import streamlit as st
import pickle
from PIL import Image
import textwrap
import google.generativeai as genai  
from IPython.display import Markdown
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline

# Define the makeTokens function as used in the ML model
def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')
        tkns_ByDot = []
        for j in range(len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))
    if 'com' in total_Tokens:
        total_Tokens.remove('com')
    return total_Tokens

# Load the trained phishing detection model
loaded_model = pickle.load(open('phishing_Detection_URL.pkl', 'rb'))

# Configure Generative AI API key
genai.configure(api_key="AIzaSyBgJBmzsjIm028lRuRUoWdRBdFXwRYGnuk")

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Function to convert chatbot response to markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Streamlit App Title
st.title("Phishing Detection & Cybersecurity Chatbot")

# Display an image
image = Image.open('images.jpeg')  
st.image(image, caption="AI + Cyber Security", use_column_width=True, width=800)  # Adjust width as needed

### Section 1: Phishing URL Detection ###
st.header("Phishing URL Detection")
st.write("Enter a URL below to predict if it's a phishing site or not.")

# URL input box
url = st.text_input("Enter the URL here:", key="url_input")

# Prediction button
if st.button("Predict URL"):
    if url:
        # Prediction using the loaded model
        prediction = loaded_model.predict([url])[0]  # Predict for a single URL
        
        # Display results based on the prediction
        if prediction == 1:  # 1 for legitimate
            st.success("This URL is predicted to be Legitimate.")
        else:  # 0 for phishing
            st.error("This URL is predicted to be Phishing.")
    else:
        st.warning("Please enter a URL.")

### Section 2: Cybersecurity Q&A Chatbot ###
st.header("Cybersecurity Q&A Chatbot")
st.write("Ask the chatbot any question related to cybersecurity!")

# Chatbot input box
chat_input = st.text_input("Ask a cybersecurity question:", key="chat_input")

# Chatbot response button
if st.button("Ask the Question"):
    if chat_input:
        # Get response from the chatbot
        response = get_gemini_response(chat_input)
        st.subheader("Chatbot Response")
        st.write(response)
    else:
        st.warning("Please enter a question for the chatbot.")
