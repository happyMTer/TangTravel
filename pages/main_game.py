# prepare finished page
# show the generated detail personal information

import streamlit as st
from model_funcs import load_document_from_directory, split_document, create_retriever, create_glm_llm, load_vector_store
import os
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory

from langchain_core.runnables.history import RunnableWithMessageHistory


import os
# from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
# from langchain_community.chat_models import ChatZhipuAI
import time

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


if "store" not in st.session_state:
    st.session_state['store'] = {}

def get_session_history(session_id:str) -> BaseChatMessageHistory:
    if session_id not in st.session_state['store']:
        st.session_state['store'][session_id] = InMemoryChatMessageHistory()
    return st.session_state['store'][session_id]


# generate personal information
def generate_info():

    # 若找不到本地向量库faiss则读入pdf文档并创建faiss向量库
    if not os.path.exists('faiss'):
        print("Local FAISS store not found, creating new FAISS store...")
        directory = "dataset/"
        documents = load_document_from_directory(directory)

        if not documents:
            print(f'No document found')
            return
    
        split_doc = split_document(documents)
        retriever = create_retriever(split_doc)

    # 若能找到则直接从faiss本地向量库中读取retriever
    else:
        print("Loading existing FAISS store...")
        retriever = load_vector_store()

    # 加载glm大模型
    os.environ["ZHIPUAI_API_KEY"] = "490b6cc959f94b827811d71622e450b9.VBtppPP2JdTLm1zN"
    
    time.sleep(0.5)     # 防止访问api过于频繁
    glm_llm = create_glm_llm()

    ### Contextualize question ###
    contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        glm_llm, retriever, contextualize_q_prompt
    )



    sys_prompt = ("你是一个唐代人物设计小助手，我需要用这些信息做一个对话式的模拟人生游戏"
        "在这里用户扮演生成的角色，你需要通过开局设定的人物信息，结合历史事件的推进和用户的选择或回答，\
            一步步推理出接下来的故事走向并与用户交互。"
        "Context:{context}"
        )
    # else:
    #     sys_prompt = ("你是一个唐代人物设计小助手，我需要用这些信息做一个对话式的模拟人生游戏"
    #         "在这里用户扮演生成的角色，你需要通过开局设定的人物信息，结合历史事件的推进和用户的选择或回答，\
    #             一步步推理出接下来的故事走向并与用户交互。"
    #         "请结合历史信息、当前身份信息和用户输入，推理出事件的走向和结果，并合理生成下一个事件(可以是几天、几个月或几年之后，也可以结合真实历史走向考虑)"
    #         "请输出事件的走向和结果，然后给出下一个事件的内容供用户继续回答"
    #         "Context:{context}"
    #         )

    # 设置用户prompt
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", sys_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    # query = "请给我返回生成人物的所有信息"

    # chain
    question_answer_chain = create_stuff_documents_chain(glm_llm, qa_prompt)
    # chain = create_retrieval_chain(retriever, question_answer_chain)

    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    # 在 chain 调用之前输出 store 字典内容
    print(f'store>>>>>>>>>>>>>>>{st.session_state['store']}')

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )
    
    return conversational_rag_chain
    


# Streamed response emulator
def response_generator(response_info):
    
    for word in response_info.split():
        yield word + " "
        time.sleep(0.05)


# with st.container():
st.header("大唐漫游vlog :sun_with_face::shaved_ice::tropical_drink:", divider='red')


if "chain" not in st.session_state:
    # st.session_state['chain'] = True
    st.session_state['chain'] = generate_info()
    query = f"""请根据以下提示生成一个唐代人的身份信息具体情况：
            性别：{st.session_state['gender']},"
            出生时段：{st.session_state['born_time']},"
            出生地域：{st.session_state['born_place']},"
            家庭阶层：{st.session_state['family_status']},"
            细节补充：{st.session_state['status_detail']},"
        请结合历史信息，根据以上提示生成一个人的具体身份信息，如出生时间（具体到年月日），\
            出生地点（根据唐代当时的行政区域划分具体到镇或县），父母工作（具体是做什么的，如果是“士”阶层那么父亲是什么官员等），\
            家庭资产（请根据阶层给出一个合理的资产），家庭关系构成（兄弟姐妹等等），还有其他一些补充的初始设定（如自带天赋、身体状况等）。"
            你的输出：请以第二人称'你'对用户介绍人物的所有信息，并生成第一个需要'你'解决的事件
            """
    response = st.session_state['chain'].invoke(
        {"input": query},
        {"configurable": {"session_id":"abc123"}},
    )

    res_info = response['answer']

    print(f'Identity:{res_info}')

    #####

    if "messages" not in st.session_state:
        st.session_state['messages'] = []
    st.session_state['messages'].append({"role": "ai", "content": res_info})

# Every epoch -> Display all the previous messages 
for msg in st.session_state['messages']:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

    #####




# start at the user submit, loop until the role's death
if prompt:=st.chat_input("我该怎么做呢..."):

    # Display user message in chat message container
    st.session_state['messages'].append({"role": "user", "content": prompt})

    with st.chat_message('user'):
        st.markdown(prompt)
    # # Add user message to chat history
 

    query = f"""请结合历史信息、当前身份信息和用户输入，推理出事件的走向和结果，并合理生成下一个事件\
            (可以是几天、几个月或几年之后，也可以结合真实历史走向考虑)
            请输出事件的走向和结果，然后给出下一个事件的内容供用户继续回答，注意生成下一个事件时由于时间变化，角色的处境也会变化。
            当到达一定年限后，合理安排人物死亡，不再生成事件。若当前人物已死亡，不管用户输入什么，全部回答：您已经去投胎啦，下辈子再来吧~
            用户的回答为：
    """
    query += prompt

    response = st.session_state['chain'].invoke(
    {"input": query},
    {"configurable": {"session_id":"abc123"}},
    )
    res_info = response['answer']
    print(f'res_info: {res_info}')

    with st.chat_message('ai'):
        st.write_stream(response_generator(res_info))

    # if "messages" not in st.session_state:
    #     st.session_state['messages'] = []
    st.session_state['messages'].append({"role": "ai", "content": res_info})




