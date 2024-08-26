# Prepare Page: Gender selection
# Show the entry of the website
import streamlit as st

with st.container():
    col_girl, col_boy = st.columns([0.5, 0.5], vertical_alignment="center")
    with col_girl:
        st.image('./images/girl.jpg', use_column_width=True)
        if st.button("girl", use_container_width=True):     # 选择了女孩身份
            st.session_state['gender'] = '女'
            
    
    with col_boy:
        st.image('./images/boy.jpg', use_column_width=True)
        if st.button("boy", use_container_width=True):      # 选择了男孩身份
            st.session_state['gender'] = '男'

with st.container():
    col_back, col_next = st.columns([1,1], vertical_alignment="center")
    with col_back:
        if st.button("Back"):
            st.switch_page("app.py")
    
    with col_next:
        if st.button("Next"):
            st.switch_page("./pages/place_time_prepare.py")
    
