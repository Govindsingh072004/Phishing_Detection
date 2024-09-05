import streamlit as st
import pickle
import requests
from PIL import Image
import textwrap
import google.generativeai as genai  
from IPython.display import Markdown

# Load the trained phishing detection model
loaded_model = pickle.load(open('phishing_Detection.pkl', 'rb'))


genai.configure(api_key="AIzaSyBgJBmzsjIm028lRuRUoWdRBdFXwRYGnuk")


def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Function to convert chatbot response to markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


st.title("Phishing Detection & Cybersecurity Chatbot")


image = Image.open('images.jpeg')  
st.image(image, caption="AI+ Cyber Security", use_column_width=50)  

### Section 1: Phishing URL Detection ###
st.header("Phishing URL Detection")
st.write("Enter a URL below to predict if it's a phishing site or not.")


url = st.text_input("Enter the URL here:", key="url_input")


if st.button("Predict URL"):
    if url:
        
        prediction = loaded_model.predict([url])

        
        if prediction == 'good':
            st.success("This URL is predicted to be Legitimate.")
        else:
            st.error("This URL is predicted to be Phishing.")
    else:
        st.warning("Please enter a URL.")

### Section 2: Cybersecurity Q&A Chatbot ###
st.header("Cybersecurity Q&A Chatbot")
st.write("Ask the chatbot any question related to cybersecurity!")


chat_input = st.text_input("Ask a cybersecurity question:", key="chat_input")


if st.button("Ask the Question"):
    if chat_input:
        
        response = get_gemini_response(chat_input)
        st.subheader("Chatbot Response")
        st.write(response)
    else:
        st.warning("Please enter a question for the chatbot.")
