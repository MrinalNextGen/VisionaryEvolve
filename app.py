import os
 
import google.generativeai as genai
# from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
genai.configure(api_key=os.getenv("google_api_key"))



  #model llms
# llm=genai.GenerativeModel("gemini_pro",) #it control the answer how much balance or  acurate answer you want
def get_gemini_response(question):
    llm=genai.GenerativeModel('gemini-pro')
    response=llm.generate_content(question)
    return response.text

st.set_page_config(page_title="q&a Demo")


st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(input)
    st.write(response)