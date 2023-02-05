import openai
import streamlit as st
import pandas as pd
import streamlit_chat
from PIL import Image
from streamlit_chat import message
import requests


openai.api_key = st.secrets["api_secret"]

#st.markdown(
#    """
#    <style>
#    .main{
#    background-color: #FF0000;
#    }
#    </style>
#    """,
#    unsafe_allow_html=True
#)


#image = Image.open("C:/Users/yoshe/fire.jpg")
#st.image(image, caption="Fire Protection Rocks")

# Using "with" notation
with st.sidebar:
    image = Image.open("C:/Users/yoshe/fire.jpg")
    st.image(image, caption="Fire Protection Rocks 	:sparkles:")


header = st.container()

with header:
    st.title('FiresafeAI')
    st.text('Welcome to my small demo :)')
    st.text('In this initial demo, only a few codes were used')
    st.text('Please feel free to leave some feedback or contact us at firesafeai@gmail.com')

st.subheader("Describe your situation or ask your question")


article_text=st.text_area("enterd text")


if len(article_text) >100 :
    temp=st.slider("temperature", 0.0,1.0,0.1)
    if st.button("Generate Summary"):
        response = openai.Completion.create(
            engine="text-ada-001",
            prompt="summarize this article"+article_text,
            max_tokens=50,
            temperature=temp,
        )


        res=response["choices"][0]["text"]
        st.info(res)

       # st.download_button("Download Result")
else:
    st.warning("This sentence is not long enough")
       

def generate_response(prompt):
    completion=openai.Completion.create(
        engine = "text-ada-001",
        prompt = prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature= 0.5,
    )

    message=completions.choices[0].text
    return message


st.title("chatbot")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 

user_input=get_text

if user_input:
    output=generate_response(user_input)
    st.session_state.past.append(user_input),
    st.session_state.generated.append()

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')



