# 唐朝漫游助手

这是一个唐朝漫游助手，在这里，你可以初始选择你想要投胎的年份、性别、地区、家庭条件等，本系统会根据你的要求自动生成符合的人物profile。
你将以一个全新的生命投入虚拟大唐中，度过完整的一生。
在此期间，你会领略到许多唐朝的风土人情，或许也会经历重大事件，有一些关键时间点的选择可能会改变你的人生轨迹。也许甚至会影响历史的发展。
等到了生命尽头，回顾你多姿多彩的一生，你是否会有新的感悟？你对大唐是否又有了全新的印象呢？

## 运行指南
1. cd path\to\the\project
2. open virtual env
3. streamlit run app.py

## 参数设置
1. Use glm-4-flash, and the API_LEY should be unique
2. Use OpenAI Embedding API, and the API_KEY should be unique
3. Use FAISS VectorStore and local pdf references to create vectorstore
4. You can change your favorite image to replace the current one
5. The dataset directory is too large that I didn't uploaded, you can download online some reference which you may want to use
