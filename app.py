import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Placement Practice" , layout = "centered")
st.title("AI Placement Assistant")
st.caption("Practice and Prepare for your Interviews")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title', ['Machine Learning Engineer','Senior Software Engineer','Data Analyst', 'Prompt Engineer', 'DevOps Engineer', 'Other'])
if role == "Other":
  st.text_input('Enter you Job Title', 'XXXXXXX')
model = st.selectbox('Model', ['openai/gpt-oss-20b','openai/gpt-oss-120b'])
level = st.selectbox('Difficulty',['Beginner', 'Intermediate', 'Advanced'])
mode = st.radio('Activity', ['Generate Questions','Generate Code Questions', 'Evaluate Answers', 'Improve Answers'])
if mode == 'Generate Questions':
  count = st.slider("Number of Questions",1,10,5)
elif mode == 'Generate Code Questions':
  topic = st.selectbox('Topics', ['SQL', 'AIML', 'Python', 'DSA', 'C++/C', 'Java', 'PHP', 'DevOps', 'Web Development', 'Cyber security'])
  count = st.slider("Number of Questions",1,10,5)
