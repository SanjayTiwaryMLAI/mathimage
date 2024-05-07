import streamlit as st
import boto3
import os
import json
import docx
from core_lib.math_question_generation import Analyticsfunction, mathquestion
from core_lib.base_function import pdfuplaodllmmodelselection

st.set_page_config(page_title="Text Summarization, Q&A, and Image Generation")

# Function to translate text
@st.cache_resource
def translate(text):
    translate = boto3.client(service_name='translate', region_name='us-east-1')
    result = translate.translate_text(Text=text, SourceLanguageCode='en', TargetLanguageCode='hi')
    return result.get('TranslatedText')

# Function to extract JSON data
def extract_json(response):
    try:
        start_index = response.find('{')
        end_index = response.rfind('}') + 1
        json_data = response[start_index:end_index]
        data = json.loads(json_data)
        return data
    except (ValueError, TypeError):
        st.error("Error: Invalid JSON data")
        return None

# Sidebar
st.sidebar.title("Options")
option = st.sidebar.selectbox("Select an option", ["Summarization", "Q&A", "Image Generation"])

# Summarization
if option == "Summarization":
    st.title("Text Summarization")
    text = st.text_area("Enter text to summarize")
    if st.button("Summarize"):
        obj = Analyticsfunction()
        claude3 = obj.call_claude_sonet_text
        math = mathquestion()
        summary = math.create_summary(text)
        st.success(summary)

# Q&A
elif option == "Q&A":
    st.title("Question & Answer")
    text = st.text_area("Enter text for Q&A")
    if st.button("Generate Questions"):
        obj = Analyticsfunction()
        claude3 = obj.call_claude_sonet_text
        math = mathquestion()
        prompt = f'''Human: Please generate 5 multiple-choice questions and their respective answers based on the content provided in the attached document. The questions should cover a range of difficulty levels (easy, medium, and hard) and test different aspects of the content, such as factual information, concepts, and analysis. Each question should have 4 answer choices, with only one correct answer
        please include question, options, answer, explanation. 
        <book>
        {text}
        </book>
        create the response in json format

        Assistant:'''
        body = json.dumps({"prompt": prompt})
        question = math.question_answer_generation(body)
        json_data = extract_json(question)
        if json_data:
            for question in json_data["questions"]:
                st.write(f"Question: {question['question']}")
                st.write(f"Options: {', '.join(question['options'])}")
                st.write(f"Answer: {question['answer']}")
                st.write(f"Explanation: {question['explanation']}")
                st.write("---")

# Image Generation
elif option == "Image Generation":
    st.title("Image Generation")
    text = st.text_area("Enter text for image generation")
    if st.button("Generate Image"):
        obj = Analyticsfunction()
        claude3 = obj.call_claude_sonet_text
        math = mathquestion()
        math.create_image(text)
        st.image(math.image_path)

# Run the app
if __name__ == "__main__":
    st.sidebar.markdown("""
    <small>Created by Anthropic</small>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("""
    <small>Powered by Streamlit</small>
    """, unsafe_allow_html=True)
    st.write("Streamlit app demonstrating text summarization, Q&A, and image generation.")
    st.sidebar.markdown("""
    <small>Note: This app requires an active internet connection and may take some time to load.</small>
    """, unsafe_allow_html=True)
    st.write("Select an option from the sidebar to get started.")
    st.stop()