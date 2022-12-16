import os
import openai
import streamlit as st
import numpy as np
import io
import qrcode
import os
import time
from PIL import Image
import pandas as pd
from streamlit_lottie import st_lottie
import json
import requests
from style1 import st_button, info_css
info_css()
def load_image(img):
    im=Image.open(img)
    return im
size=20
# st.title('CODE GENERATOR')
st.markdown("<h1 style='text-align: center; color: white;'>Code Generator 💬</h1>", unsafe_allow_html=True)
st.markdown("---")
with st.sidebar:
    st.write("OpenCode")

platform=st.selectbox("Select the Platform of Question:", ("Leetcode", "CodeChef", "Hackerrank"))
language=st.selectbox("Select the Language of Solution:", ("C++", "Python", "Java"))
ques=st.text_area("Input the Question Here")
button=st.button("Generate")



def gen_auto_response(ques):
    openai.api_key = "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"
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
