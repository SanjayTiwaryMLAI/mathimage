
import streamlit as st
import boto3
import os
import json
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from core_lib.math_question_generation import Analyticsfunction, mathquestion
from core_lib.base_function import pdfuplaodllmmodelselection

st.set_page_config(page_title="Text Summarization, Q&A, and Image Generation", layout= "wide")

#write the name of solution
st.title("Math Class-Text Summarization, Q&A, and Image Generation")

# Global variable to store the summary
summary = ""

def create_image(question):
    math = mathquestion()
    detect_shape = math.detect_shape
    shape = detect_shape(question)

    prompt = f'''Human: write python code to draw {shape} for generating image for the {question} using matplotlib package
                1. Save plot as {shape}.jpg, plot context/question at top. create small image with fixed size pixels
                2. context into the image at top. 
                3. draw correct shape for {shape}
                4. complete all edges and align properly for {shape}
                5. Label each edge with (e.g., A, B, etc.) for better understanding.
                6. import all necessary libraries and functions.
                7. write code to draw {shape}
                8. code should be 100% accurate
    
                Assistant:'''

    body = json.dumps({"prompt": prompt})
    text = math.call_claude_sonet_text(body)
    image_name = f'{shape}.jpg'
    output_file = f'{shape}.py'
    math.extract_python_code(text, output_file)
    time.sleep(3)
    os.system(f"python3 {output_file}")
    time.sleep(5)

    # Check if the image file exists
    if os.path.isfile(image_name):
        img = mpimg.imread(image_name)
        st.image(img, width=400)
    else:
        st.write(f"Error: Image file '{image_name}' not found.")


# Function to translate text
@st.cache_resource
def translate(text, source_lang='en', target_lang='hi'):
    translate = boto3.client(service_name='translate', region_name='us-east-1')
    result = translate.translate_text(Text=text, SourceLanguageCode=source_lang, TargetLanguageCode=target_lang)
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

# Sidebar 📋
st.sidebar.title("Options 🛠️")

# Language selection
languages = ['en', 'hi', 'es', 'fr', 'de', 'zh', 'ja', 'ru', 'pt', 'ar']
selected_lang = st.sidebar.selectbox("Select Language", languages, index=languages.index('en'))

num_questions = st.number_input("Enter the number of questions to generate", min_value=1, max_value=10, value=1)

# Ask question button
question = st.text_input("Enter your question:")
ask_question_button = st.button("Ask Question")
if ask_question_button:
    create_image(question)

# # Always display on Streamlit UI 📺

# # st.title("<h1 style='font-size: 30px;'>Upload Input Text 📥</h1>", unsafe_allow_html=True)
# # import streamlit as st

# import streamlit as st

st.markdown("<h1 style='font-size: 30px; color: blue;'>Upload Input Text 📥</h1>", unsafe_allow_html=True)


#change the font size

input_text = st.file_uploader("Upload a text file 📂", type=["txt"], )
#display the content of uploaded file name


if input_text is not None:
    # Summarization ✂️
    start_summarization = st.button("Start Summarization 🚀")
    if start_summarization:
        st.markdown("<h1 style='font-size: 30px; color: blue;'>Text Summarization 📝</h1>", unsafe_allow_html=True)
        text = input_text.read().decode('utf-8')
        obj = Analyticsfunction()
        claude3 = obj.call_claude_sonet_text
        math = mathquestion()
        summary = math.create_summary(text)
        st.write(translate(summary, target_lang=selected_lang))
        # Always keep the summary on UI 📋
        st.session_state.summary = summary
        # Write to local 💾
        with open('summary.txt', 'w') as f:
            f.write(summary)

    # Q&A ❓
    start_qa = st.button("Start Question & Answer 🤔")
    math = mathquestion()
    # Read summary.txt
    with open('summary.txt', 'r') as f:
        summary = f.read()
    if start_qa:
        st.markdown("<h1 style='font-size: 30px; color: blue;'>Question & Answer ❓❔</h1>", unsafe_allow_html=True)
        # st.title("Question & Answer ❓❔")
        #get user input to decide on number of question 

        prompt = f'''Human: Please generate {num_questions} multiple-choice questions and their respective answers based on the content provided in the attached document. The questions should cover a range of difficulty levels (easy, medium, and hard) and test different aspects of the content, such as factual information, concepts, and analysis. Each question should have 4 answer choices, with only one correct answer. Please include question, options, answer, and explanation. 
            <book>
            {summary}
            </book>
            Please create the response in JSON format.

            Assistant:'''
        body = json.dumps({"prompt": prompt})
        question = math.question_answer_generation(body)
        json_data = extract_json(question)
        #parse Json data and display on UI
        st.write(json_data)

  
        # Save json_data to local

        if json_data and "questions" in json_data:  # Check if json_data is defined and has "questions" key ✅
            for question in json_data["questions"]:
                st.write(f"Question: {translate(question['question'], target_lang=selected_lang)} ❓")
                create_image(question["question"])  # Fixed image size
                #options = [translate(option, target_lang=selected_lang) for option in question['options']]
                st.write(f"Options: {question['options']} 🔽")
                st.write(f"Answer: {question['answer']} ✅")
                st.write(f"Explanation: {translate(question['explanation'], target_lang=selected_lang)} 💡")
                st.write("--------------------------------------")
        else:
            st.warning("Please generate a summary first. ⚠️")


# Run the app
if __name__ == "__main__":
    st.sidebar.markdown("""
    <small>Created by Anthropic</small>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("""
    <small>Powered by Streamlit</small>
    """, unsafe_allow_html=True)
    #st.write("Streamlit app demonstrating text summarization, Q&A, and image generation.")
    st.sidebar.markdown("""
    <small>Note: This app requires an active internet connection and may take some time to load.</small>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("Question1 : ABCDEF is a hexagon (six-sided polygon). Find the value of AB+BC+CD+DE+AF+FE+AE ?")

    st.sidebar.markdown("Question2: If the position vectors of the vertices A, B, and C of a triangle △ABC are αi+βj+γk, βi+γj+αk, and γi+αj+βk respectively, then △ABC is ")
    #st.write("Upload an input text file to get started.")
    st.stop()