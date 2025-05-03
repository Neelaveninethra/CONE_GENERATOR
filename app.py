import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
groq_api_key=os.getenv("GROQ_API_KEY")

llm=ChatGroq(api_key=groq_api_key,model="gemma2-9b-it")

prompt="""You are an expert programmer. Generate code for the following task in {language}:

Task: {task}

Make sure the code is:
- Clean and readable
- Includes comments
- Solves the problem as described
"""

prompt=PromptTemplate(template=prompt,input_variables=["language","task"])

st.title("Code Generator")

task=st.text_input("Enter the task")
language=st.text_input("Enter the language")


if st.button("Generate Code"):
    if task and language:
        with st.spinner("Generating code..."):
            response = llm.invoke(prompt.format(language=language, task=task))
            st.write(response.content)
    else:
        st.write("Please enter a task and language")
