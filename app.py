from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#Configure API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Google gemini model and provide sql query as response
def get_gemini_pro(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    #response=model.generate_content([prompt[0],question])
    response = model.generate_content(prompt + [question])
    return response.text

#Function to retrieve query from the sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


#Define a prompt
prompt=[
    """
    You are an expert in converting English questions to SQL Query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, AND MARKS \n\n
    For Example, \n Example 1 - How many entries of record are present, the SQL query would be something like this
    Select count(*) from Student; \n
    Example 2 - Tell me all the students studying in Data Science Class?,
    the sql Command will be something like this Select * from STUDENT where CLASS = "Data Science";
    also the SQL code should not have '''   in beginning or end and sql word in output
    """
]

#Streamlit app
st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input:", key="input")

submit = st.button("Ask the question")

#if submit is clicked
if submit:
    response = get_gemini_pro(question,prompt)
    print(response)

    data = read_sql_query(response, "student.db")
    st.subheader("The Response is:")
    for row in data:
        print(row)
        st.write(row)