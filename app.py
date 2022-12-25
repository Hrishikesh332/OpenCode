import openai
import streamlit as st
from PIL import Image

def load_image(img):
    im=Image.open(img)
    return im
size=20

st.markdown("<h1 style='text-align: center; color: white;'>OpenCode 💬</h1>", unsafe_allow_html=True)
st.markdown("---")
with st.sidebar:
    st.image("ai.jpeg")
    st.title("OpenCode")
    st.caption('''
    OpenCode aims to provide solution of any programming question according to the user needs. Opencode is developed for the students struggling while learning.
    ''', unsafe_allow_html=False)
   

platform=st.selectbox("Select the Platform of Question:", ("Leetcode", "CodeChef", "Hackerrank"))
language=st.selectbox("Select the Language of Solution:", ("Python", "C++", "Java"))
ques=st.text_area("Input the Question Here")
button=st.button("Generate")



def gen_auto_response(ques):
    openai.api_key=st.secrets["api"]
    
    response = openai.Completion.create(
        model="code-cushman-001",
        prompt=f""""Given a Python solution for the leetcode question below
                    {platform} Question: {ques}
                    {language} Solution: """,
        temperature=0,
        max_tokens=1114,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    print(response)
    return response.choices[0].text

if ques and button:
    with st.spinner("-------Generating Code------"):
        reply=gen_auto_response(ques)
        st.code(reply)
        
        button2=st.button("Explain Code")
        






