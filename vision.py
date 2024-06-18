import os
 
import google.generativeai as genai
# from langchain.llms import OpenAI
from dotenv import load_dotenv
from PIL import Image
import streamlit as st

load_dotenv()
genai.configure(api_key=os.getenv("google_api_key"))



  #model llms
# llm=genai.GenerativeModel("gemini_pro",) #it control the answer how much balance or  acurate answer you want
llm=genai.GenerativeModel('gemini-pro-vision')
chat=llm.start_chat(history=[])
def get_gemini_response(input,image):
    if input!= "" :
    #  response=llm.generate_content([input,image])
     response=chat.send_message([input,image])
    else:
      # response=llm.generate_content(image)
      response=chat.send_message(image)
    return response

st.set_page_config(page_title="q&a Demo")


st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
   st.session_state['chat_history']=[]

input=st.text_input("Input: ",key="input")
uploaded_file = st.file_uploader("choose an image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image,caption="uploded image",use_column_width=True)

submit=st.button("tell me about the image")

if submit and input:
    response=get_gemini_response(input,image)
    st.session_state['chat_history'].append(("you",input))
    st.subheader("the response is ")

    for chunk in response:

     st.write(chunk.text)
     st.session_state['chat_history'].append(("bot",chunk.text))
st.subheader("chat history is")
for role,text in st.session_state['chat_history']:
  st.write(f"{role}:{text}")


