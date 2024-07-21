import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import openai 
import os
from dotenv import load_dotenv
load_dotenv()

#Langsmith Tracking
os.environ['langchain_api_key'] = os.getenv('langchain_api')
os.environ['langchain_tracing_v2'] = "True"
os.environ['Langchain_project'] = "Q&A Chatbot with OpenAI"

#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", '''You are my Linkedin Connection request message creator. I will give input the name and bio of the person. Create me a message with 250 characters. Include humbleness and humility in the message'''),
        ('user', "Enter Details: {details}")
    ]
)

def get_response(details, api_key, engine, temperature, max_tokens):
   # openai.api_key = api_key
    llm = ChatOpenAI(model_name = engine, openai_api_key=api_key)
    parser = StrOutputParser()
    chain = prompt|llm|parser
    answer = chain.invoke({'details': details})
    return answer

#Title of the app
st.title("LinKer - LinkedIN message creator")

#Sidebar
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type = "password")

#Dropdown to select OpenAI Models
engine = st.sidebar.selectbox("Select your model",['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo'])

#Adjust temperature and max_tokens
temperature  = st.sidebar.slider("Temperature", min_value = 0.0, max_value=1.0, value = 0.8)
max_tokens = st.sidebar.slider("Max Tokens", min_value = 50, max_value = 300, value = 150)

#Main interface for user input
st.write("Let's create the message")
user_input = st.text_input("You:")

if user_input:
    if api_key:
        try:
            response = get_response(user_input, api_key, engine, temperature, max_tokens)
            st.write(response)
        except Exception as e:
            st.write(f"An error occurred: {e}")
    else:
        st.write("Please provide the OpenAI API key")
else:
    st.write("Please provide the details")