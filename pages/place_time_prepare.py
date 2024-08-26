# Prepare born time and born place information

import streamlit as st
import datetime

time_list = ["开国统一","贞观之治", "帝后共治", "开元盛世", "盛极而衰", "中唐困局", "宦党争权", "末唐崩乱"]
place_list = ['京畿道', '关内道', '都畿道', '河南道', '河东道', '河北道',
                      '山南西道', '山南东道', '淮南道', '江南东道', '江南西道',
                      '黔中道', '陇右道', '剑南道', '岭南道']

# # 设置时间下拉框选项
# def set_time_select_box(list):
    
#     if 'born_time' not in st.session_state:
#         time_option = st.selectbox(label="label", options=list, index=0, label_visibility="collapsed")
    
#     else:
#         index = list.index(st.session_state['born_time'])
#         time_option = st.selectbox(label="label", options=list, index=index, label_visibility="collapsed")
    
#     st.session_state['born_time'] = time_option


# 设置下拉框选项
def set_select_box(session_key, list):
    key = session_key + '_key'
    if session_key == 'born_time':
        if session_key not in st.session_state:
            time_option = st.selectbox(label="label", options=list, index=0, key=key, label_visibility="collapsed")
        else:
            print(f'{datetime.datetime.now()}: {session_key} 当前选择了 {st.session_state[session_key]}')
            time_index = list.index(st.session_state[session_key])
            time_option = st.selectbox(label="label", options=list, index=time_index, key=key, label_visibility="collapsed")
        st.session_state[session_key] = time_option
        print(f'{datetime.datetime.now()}: 修改{session_key}为 {st.session_state[session_key]}')
    
    elif session_key == 'born_place':
        if session_key not in st.session_state:
            place_option = st.selectbox(label="label", options=list, index=0, key=key, label_visibility="collapsed")
        else:
            print(f'{datetime.datetime.now()}: {session_key} 当前选择了 {st.session_state[session_key]}')
            place_index = list.index(st.session_state[session_key])
            place_option = st.selectbox(label="label", options=list, index=place_index, key=key, label_visibility="collapsed")
        st.session_state[session_key] = place_option
        print(f'{datetime.datetime.now()}: 修改{session_key}为 {st.session_state[session_key]}')        


# # 设置地点下拉框选项
# def set_place_select_box(list):
    
#     if 'born_place' not in st.session_state:
#         place_option = st.selectbox(label="label", options=list, index=0, label_visibility="collapsed")
    
#     else:
#         index = list.index(st.session_state['born_place'])
#         place_option = st.selectbox(label="label", options=list, index=index, label_visibility="collapsed")
    
#     st.session_state['born_place'] = place_option



with st.container():
    st.header("Now please choose your Native Place & Date of birth!:blue[cool] :sunglasses:", divider='gray')
    col_left, col_right = st.columns([1,1], vertical_alignment='center', gap='medium')

    with col_left:
        st.subheader('请选择你的出生时间>>>', divider='orange')
        set_select_box('born_time', time_list)
        # print(f'你选择了{option}')

    with col_right:
        st.subheader('请选择你的出生地点>>>', divider='blue')
        set_select_box('born_place', place_list)

with st.container():
    col_back, col_next = st.columns([1,1], vertical_alignment="center")
    with col_back:
        if st.button("Back"):
            st.switch_page("./pages/gender_prepare.py")
    with col_next:
        if st.button("Next"):
            st.switch_page("./pages/status_prepare.py")
            # choice(details)
