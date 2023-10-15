# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('AI 시인')

content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 쓰기!'):
        with st.spinner('시를 작성 중입니다..'):
            result = chat_model.predict(content + "에 대한 시를 써주세요.")
            st.write(result)