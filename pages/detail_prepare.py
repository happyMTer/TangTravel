# 补充一些其他细节信息（可选）
import streamlit as st

@st.dialog("身份信息确认")
def choice():
    st.header("你的选择>>>", divider='blue')
    st.write(f"性别：{st.session_state['gender']}")
    st.write(f"籍贯：{st.session_state['born_time']}, {st.session_state['born_place']}")
    st.write(f"家庭条件：{st.session_state['family_status']}")
    st.write(f"细节补充：{st.session_state['status_detail']}")
    if st.button("Submit"):
        st.switch_page("./pages/main_game.py")


with st.container():
    st.header("补充一些其他细节信息吧:blue[cool] :sunglasses:", divider="green")
    details = st.text_area(label="text", label_visibility='collapsed', value="", 
                max_chars=500, placeholder="请给我一些细节(可以不写)")
    
    st.session_state['status_detail'] = details

    with st.container():
        col_back, col_next = st.columns([1,1], vertical_alignment='center', gap='medium')
    
    with col_back:
        if st.button("Back", use_container_width=True):
            st.switch_page('./pages/status_prepare.py')
    with col_next:
        if st.button("Next", use_container_width=True):
            choice()
    
    
