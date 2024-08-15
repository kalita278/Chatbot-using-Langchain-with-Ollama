import requests
import streamlit as st


def get_promt1_response(input_text):
    response = requests.post("http://localhost:8501/summary/invoke",
                             json={'input':{'topic':input_text}})
    
    return response.json()['output']['content']

def get_promt2_response(input_text):
    response = requests.post("http://localhost:8501/poem/invoke",
                             json={'input':{'topic':input_text}})
    
    return response.json()['output']

st.title('Demo langchain llama2 chatbot')
input_text1= st.text_input("Write a summary on")
input_text2 = st.text_input("write a poem on")

if input_text1:
    st.write(get_promt1_response(input_text1))
if input_text2:
    st.write(get_promt2_response(input_text2))