import os
from apikey import api_key 
import streamlit as st 
from io import StringIO
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = api_key

st.markdown("<h1 style='text-align: center; color: White;'>🤖 AI's Prespective Case Suggestions</h1>", unsafe_allow_html=True)
st.subheader('Upload your Case:')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.subheader('The Case:')
    string_data = stringio.read()
    st.write(string_data)

    st.subheader('How can I assist you with this case:') 
    Ad = st.text_input("")
    if Ad and len(Ad) > 12:
        prompt = Ad+" "+string_data
        llm = OpenAI(temperature=0.9) 
        st.subheader("AI's suggestions:")
        response = llm(prompt)
        st.write(response)
