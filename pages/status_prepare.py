# prepare the status

import streamlit as st



with st.container():
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.image('./images/girl.jpg', use_column_width=True)
        if st.button("士", use_container_width=True):
            st.session_state['family_status'] = "士"

        st.image('./images/boy.jpg', use_column_width=True)
        if st.button("农", use_container_width=True):
            st.session_state['family_status'] = "农"


    with col2:
        st.image('./images/girl.jpg', use_column_width=True)
        if st.button("工", use_container_width=True):
            st.session_state['family_status'] = "工"

        st.image('./images/boy.jpg', use_column_width=True)
        if st.button("商", use_container_width=True):
            st.session_state['family_status'] = "商"
 

    with col3:
        st.image('./images/girl.jpg', use_column_width=True)
        if st.button("杂", use_container_width=True):
            st.session_state['family_status'] = "杂"

        st.image('./images/boy.jpg', use_column_width=True)
        if st.button("其他", use_container_width=True):
            st.session_state['family_status'] = "其他"   

with st.container():
    col_back, col_next = st.columns([1,1], vertical_alignment="center")
    with col_back:
        if st.button("Back"):
            st.switch_page("./pages/place_time_prepare.py")
    with col_next:
        if st.button("Next"):
            st.switch_page("./pages/detail_prepare.py")

    
        