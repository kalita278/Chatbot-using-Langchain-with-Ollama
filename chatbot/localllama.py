from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')


prompt = ChatPromptTemplate.from_messages(
[

  ('system','you are a helpful assistant. Please respond to the user queries.'),
  ('user','Questions,{question}')
]
)

st.title('Lanchain Demo with LLama2')
input_text = st.text_input('enter your text')


llm = Ollama(model='llama2')
op_parser = StrOutputParser()
chain = prompt|llm|op_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))