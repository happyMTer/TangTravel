import streamlit as st



with st.container():
    col_left, col_right = st.columns([0.7, 0.3])
    with col_left:
        st.title("这是一个唐朝漫游助手:blue[cool] :sunglasses:")
        st.write("在这里，你可以初始选择你想要投胎的年份、性别、地区、家庭条件等，本系统会根据你的要求自动生成符合的人物profile。\
                你将以一个全新的生命投入虚拟大唐中，度过完整的一生。")
        st.subheader(":notes:虚拟大唐:ferris_wheel:等你来游:notes:")
        st.write("在此期间，你会领略到许多唐朝的风土人情，或许也会经历重大事件，有一些关键时间点的选择可能会改变你的人生轨迹。\
                 也许甚至会影响历史的发展。")
        st.write("等到了生命尽头，回顾你多姿多彩的一生，你是否会有新的感悟？你对大唐是否又有了全新的印象呢？")

        # st.image("./images/back_index_left.jpg", use_column_width = True)
    
    with col_right:
        st.title("入口在这里哦:feet::feet::feet:")
        if st.button(label="Start", use_container_width=True):
            st.switch_page("pages/gender_prepare.py")

