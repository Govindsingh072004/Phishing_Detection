import streamlit as st
import pickle
import requests
from PIL import Image
import textwrap
import google.generativeai as genai  # Hypothetical Gemini API module (placeholder)
from IPython.display import Markdown

# Load the trained phishing detection model
loaded_model = pickle.load(open('phishing_Detection.pkl', 'rb'))

# Configure the hypothetical Google Gemini API (replace with the actual API when available)
genai.configure(api_key="AIzaSyBgJBmzsjIm028lRuRUoWdRBdFXwRYGnuk")

# Function to call the Gemini API (placeholder function)
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Function to convert chatbot response to markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Title of the app
st.title("Phishing Detection & Cybersecurity Chatbot")

### Adding an Image at the Top of the App ###
# Load an image from your local system or use an online URL
image = Image.open('images (1).jpeg')  # Replace with your local image or use a URL
st.image(image, caption="AI+ Cyber Security", use_column_width=50)  # Adjust the size as needed

### Section 1: Phishing URL Detection ###
st.header("Phishing URL Detection")
st.write("Enter a URL below to predict if it's a phishing site or not.")

# Input field for the URL
url = st.text_input("Enter the URL here:", key="url_input")

# Predict button for phishing detection
if st.button("Predict URL"):
    if url:
        # Make prediction using the phishing detection model
        prediction = loaded_model.predict([url])

        # Display the result
        if prediction == 'good':
            st.success("This URL is predicted to be Legitimate.")
        else:
            st.error("This URL is predicted to be Phishing.")
    else:
        st.warning("Please enter a URL.")

### Section 2: Cybersecurity Q&A Chatbot ###
st.header("Cybersecurity Q&A Chatbot")
st.write("Ask the chatbot any question related to cybersecurity!")

# Input field for chatbot question
chat_input = st.text_input("Ask a cybersecurity question:", key="chat_input")

# Submit button for chatbot
if st.button("Ask the Question"):
    if chat_input:
        # Get response from the chatbot using the hypothetical Gemini API
        response = get_gemini_response(chat_input)
        st.subheader("Chatbot Response")
        st.write(response)
    else:
        st.warning("Please enter a question for the chatbot.")
