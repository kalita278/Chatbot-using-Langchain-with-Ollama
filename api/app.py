from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from langserve import add_routes


load_dotenv()


app = FastAPI()

model = Ollama(model='llama2')

prompt1 = ChatPromptTemplate.from_template("Write a short summary within 200 words on {topic} for children")
prompt2 = ChatPromptTemplate.from_template("Write a poem on {topic} for children")

add_routes(app,prompt1|model,path='/summary')
add_routes(app,prompt2|model,path='/poem')


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8501)