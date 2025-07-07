from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv() #to load .env  file

gemini_api_key = os.getenv("GEMINI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

if gemini_api_key:
    os.environ["GEMINI_API_KEY"] = gemini_api_key

if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

os.environ["LANGCHAIN_TRACING_V2"] = "true"
#prompt template:
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant.Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title("Langchain Demo with GEMINI API")
input_text = st.text_input("search anything")

#gemini llm:

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature = 0.7, google_api_key=os.getenv("GEMINI_API_KEY"))
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))