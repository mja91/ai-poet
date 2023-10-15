# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.set_page_config(page_title="AI 시인 📖", layout="wide")
st.title('AI 시인 📖')

content = st.text_input('시의 주제를 제시해주세요. 시가 작성된 이후 새로운 제시어를 입력하고 Enter를 입력하여 새로운 시를 작성할 수 있습니다.')

class SessionState:
    def __init__(self):
        self.button_clicked = False

try:
    state = st.session_state["state"]
except KeyError:
    state = SessionState()
    st.session_state["state"] = state

if not state.button_clicked:
    if st.button('시 작성하기'):
        state.button_clicked = True
else:
    with st.spinner('시를 작성 중입니다..'):
        result = chat_model.predict(content + "에 대한 시를 써주세요.")
        st.write(result)
        state.button_clicked = False
