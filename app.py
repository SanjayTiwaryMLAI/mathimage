
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

# Text input
st.title("Upload Input Text")
input_text = st.file_uploader("Upload a text file", type=["txt"])

if input_text is not None:
    # Summarization
    st.title("Text Summarization")
    text = input_text.read().decode('utf-8')
    obj = Analyticsfunction()
    claude3 = obj.call_claude_sonet_text
    math = mathquestion()
    summary = math.create_summary(text)
    st.success(summary)

    # Q&A
    st.title("Question & Answer")
    prompt = f'''Human: Please generate 5 multiple-choice questions and their respective answers based on the content provided in the attached document. The questions should cover a range of difficulty levels (easy, medium, and hard) and test different aspects of the content, such as factual information, concepts, and analysis. Each question should have 4 answer choices, with only one correct answer
    please include question, options, answer, explanation. 
    <book>
    {summary}
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
    st.title("Image Generation")
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
    st.write("Upload an input text file to get started.")
    st.stop()