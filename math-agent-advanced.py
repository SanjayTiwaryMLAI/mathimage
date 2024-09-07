
import os
import time
import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler
import boto3
import logging
import uuid
import botocore
import pprint
from core_lib.math_question_generation import Analyticsfunction, mathquestion

math = mathquestion()


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>👨‍⚕️ Math Problem - Amazon Bedrock Agent 🚀</h1>", unsafe_allow_html=True)

client = boto3.client('bedrock-agent-runtime',  region_name="ap-south-1")

agent_alias_id = os.environ.get('AGENT_ALIAS_ID', 'UQRJQTLPOQ')
agent_id = os.environ.get('AGENT_ID', 'IOWFOMIXO9')
session_id = str(uuid.uuid1())  # random identifier
enable_trace = True
input_text = ""
agent_response = ""

@st.cache_data
def get_type(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'type':
                return value
            else:
                result = get_type(value)
                if result is not None:
                    return result

def generate_new_session_id():
    new_session_id = str(uuid.uuid4())
    return new_session_id

# Define function to get agent response

def get_agent_response(input_text):
    # invoke the agent API
    response = client.invoke_agent(
        inputText=input_text,
        agentId=agent_id,
        agentAliasId=agent_alias_id,
        sessionId=session_id,
        enableTrace=enable_trace
    )

    logger.info(pprint.pprint(response))

    import json
    event_stream = response['completion']
    final_answer = ""

    try:
        for event in event_stream:
            if 'chunk' in event:
                data = event['chunk']['bytes']
                logger.info(f"Final answer -&gt;\n{data.decode('utf8')}")
                final_answer += data.decode('utf8')
            elif 'trace' in event: 
                #add rotating icon for wait timer on  Streamlit UI
                with st.spinner("Wait for it..."):
                    time.sleep(1)
                model_input_type = get_type(event['trace'])
                if model_input_type != None:
                    with st.expander(f"{model_input_type}", expanded=False):
                        st.json(event['trace']['trace'])
                        
            else:
                raise Exception("unexpected event.", event)
    except Exception as e:
        raise Exception("unexpected event.", e)


    return final_answer

with st.sidebar:
    st.subheader("Questions")
    
    st.write('''1. The text in the image says: "Find the number of zeroes after the decimal in 3^-100 (Given log10 3 = 0.4771).
(α) 46 (b) 47 (C) 48 (d) None of these''')
    

    
    
obj = Analyticsfunction()
    
convert_image =  obj.convert_image_to_base64
claude3 = obj.call_claude_sonet
    
def invoke_model(question, image):
    base64_image = convert_image(image)
    response = claude3(base64_image,question)
    
    
    # st.download_button(data=response, label="download")
    
    return response
            
    
#Display image
def display_image(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
    st.image(image_data, use_column_width=True)
    
def extract_text_between_quotes(text):
    start = text.find('"')
    end = text.rfind('"')
    
    if start == -1 or end == -1:
        return ""
    
    return text[start+1:end]


# question_prompt = "Your task is to extract only the text of the question and answer from the image, the image contain graduate level math images wwritten in hand or print both "

# image = st.file_uploader("UPLOAD A IMAGE")
# if image:
#     st.write("Image uploaded successfully")
#     output = open("file01.jpg", "wb")
#     output.write(image.read())
#     output.close()
#     display_image("file01.jpg") 
#     response = invoke_model(question_prompt,"file01.jpg")
#     new_agent_prompt = f"Please solve the following problem and provide the solution in a detailed, step-by-step manner. Ensure each step is clearly explained, and include the final answer in bold. The explanation should be thorough enough for someone at a graduate level to understand the reasoning and methodology behind each step. Here's the problem /n/n {response}"
#     #extract the text from response
#     #extracted_text = extract_text_between_quotes(response)
#     st.write(response)
#     #st.write(extracted_text)
#     #add a button to trigger the function
#     if st.button("Get Answer"):
#         st.write(math.call_claude_sonet_text_s35(new_agent_prompt))
#         st.write(get_agent_response(new_agent_prompt))
    

question_prompt = "Your task is to extract only the text of the question and answer from the image, the image contain graduate level math images written in hand or print both "

image = st.file_uploader("UPLOAD A IMAGE")
if image:
    st.write("Image uploaded successfully")
    output = open("file01.jpg", "wb")
    output.write(image.read())
    output.close()
    display_image("file01.jpg") 
    response = invoke_model(question_prompt, "file01.jpg")
    new_agent_prompt = f"Please solve the following problem and provide the solution in a detailed, step-by-step manner. Ensure each step is clearly explained, and include the final answer in bold. The explanation should be thorough enough for someone at a graduate level to understand the reasoning and methodology behind each step. Here's the problem:\n\n{response}"
    st.write(response)
    prompt = f"""You are an advanced AI mathematics problem-solving agent specializing in graduate-level problem-solving. You communicate at a PhD level in mathematics. When presented with a problem, always start your response with "Thanks for the interesting problem! Here is my step-by-step solution:"
            Then, use a chain-of-thought (COT) approach to solve the problem, showing each step of your reasoning process in detail. Your response should be structured, with numbered steps and the final answer bolded. Additionally, aim to explain the concepts and justifications behind each step to demonstrate a deep understanding of the subject matter
            Provide a clear and easy-to-follow example to illustrate the desired format and level of detail expected in your response.
            Please solve the following problem and provide the solution in a detailed, step-by-step manner. Ensure each step is clearly explained, and include the final answer in bold. The explanation should be thorough enough for someone at a graduate level to understand the reasoning and methodology behind each step. Here's the problem:\n\n{response}"""

    # Add radio buttons for selecting the model
    model_choice = st.radio("Choose the model for the answer:", ("Sonnet3.5", "Bedrock Agent"))

    # Add a button to trigger the function
    if st.button("Get Answer"):
        if model_choice == "Sonnet3.5":
            st.write("Anthropic Sonnet3.5 Response:")
            st.write(math.call_claude_sonet_text_s35(prompt))
        else:
            st.write("Bedrock Agent Response:")
            st.write(get_agent_response(new_agent_prompt))
                    
prompt = st.chat_input("How can I help?")
if prompt:
    # Concatenate chat history with the current user input
    with st.chat_message("user"):
        st.markdown(f"**{prompt}**")
    
    with st.chat_message("assistant"):
        response = get_agent_response(prompt)
        st.markdown(f"{response}")