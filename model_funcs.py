# from langchain import OpenAI
# from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import os
from langchain_core.documents import Document
# from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.chat_models import ChatZhipuAI
# from LLM import Yuan2_LLM

# 加载txt和pdf文档
def load_document_from_directory(directory):
    documents = []
    for filename in os.listdir(directory):    
        filepath = os.path.join(directory, filename)
        print(f'{filepath}')
        if filename.endswith('.txt'):
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
                documents.append(Document(page_content = text))
            # loader = TextLoader(filepath)
            # loader_document = loader.load()
            # documents.extend(loader_document)     # Load data into Document objects.
        elif filename.endswith('.pdf'):
            loader = PyMuPDFLoader(filepath)
            loader_document = loader.load()
            documents.extend(loader_document)     # Load data into Document objects.

    return documents


# 分割文档为chunks
def split_document(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len,
        is_separator_regex = False,
    )

    texts = text_splitter.create_documents([doc.page_content for doc in documents])
    # print(f'texts:{texts}')
    return texts


# 构建文档检索器
# 使用FAISS创建向量库，基于OpenAI的嵌入进行检索
def create_retriever(documents):
    embeddings = OpenAIEmbeddings(
        openai_api_key="---",
        openai_api_base="---"
        )
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local('faiss')
    retriever = vectorstore.as_retriever()
    return retriever

# 加载本地向量库
def load_vector_store():
    # 这里使用 OpenAI 的方法 OpenAIEmbeddings 来进行向量化。
    embeddings = OpenAIEmbeddings(
    openai_api_key="---",
    openai_api_base="---"
    )
    vectorstore = FAISS.load_local('faiss', embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()

    return retriever

os.environ["ZHIPUAI_API_KEY"] = "---"

# 创建 GLM-4-Flash LLM 实例
def create_glm_llm():
    chat = ChatZhipuAI(
        model = "glm-4-flash",
        temperature = 0.7,
    )

    return chat


