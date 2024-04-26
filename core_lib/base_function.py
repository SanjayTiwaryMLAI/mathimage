# importing required modules 
from PyPDF2 import PdfReader
import boto3
import json
from IPython.display import display_markdown,Markdown,clear_output
import tiktoken
import base64
import streamlit as st

from botocore.exceptions import ClientError
import logger

boto3_bedrock = boto3.client('bedrock', region_name='us-east-1')
bedrock_runtime = boto3.client('bedrock-runtime',region_name='us-east-1')

modelselected = "anthropic.claude-v2"

def count_tokens(string: str) -> int:
    encoding_name = "p50k_base"
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

## 1. Create function for converting pdf to text
def create_text(doc1,filename):
    doc = PdfReader(doc1) 
    text = ""
    # printing number of pages in pdf file 
    print(len(doc.pages))
    # getting a specific page from the pdf file 
    for i in range(len(doc.pages)): 
        page = doc.pages[i]
        text+= page.extract_text() 
    # extracting text from page 
    with open(filename, 'w') as f:
        f.writelines(text)
    return text

def pdfuplaodllmmodelselection(modelid, question,text, maxt, t):
    try:
        # doc = PdfReader(doc1) 
        # text = ""
        # # getting a specific page from the pdf file 
        # for i in range(len(doc.pages)): 
        #     page = doc.pages[i]
        #     text+= page.extract_text() 
        # with open("new.txt", 'w') as f:
        #     f.writelines(text)
        

        prompt_data = f"Human: {question}" + """The following is a friendly conversation between a human and an AI. 
            The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it 
            does not know. """ + f"{text}" + """\n\nAssistant:"""
        
        #prompt_data = "Human:"+ question + "on the context" + text + "Assistant:"
        body = {
                "prompt": prompt_data,
                "max_tokens_to_sample": maxt,
                "temperature": t,
                "stop_sequences": ["\n\nHuman:"],
            }
    
        modelId = modelid  # change this to use a different version from the model provider
        accept = "application/json"
        contentType = "application/json"

        response = bedrock_runtime.invoke_model(body=json.dumps(body), modelId=modelId, accept=accept, contentType=contentType)
        response_body = json.loads(response.get("body").read())
        #print(response_body.get("completion"))
        return response_body.get("completion")
    
    except ClientError:
            logger.error("Couldn't invoke Anthropic Claude")
            raise


#create a function to translate into hindi language
def translate_to_hindi(text):
    translate = boto3.client(service_name='translate', region_name='us-east-1')
    result = translate.translate_text(Text=text, SourceLanguageCode='en', TargetLanguageCode='hi')
    return result.get('TranslatedText')


#create function to detect overall sentiments and entity using comprehend
def detect_sentiment(text):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    result = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    return result.get('Sentiment')

#create function to mask detect and mask PII using comprehend
def mask_pii(text):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    result = comprehend.detect_pii_entities(Text=text, LanguageCode='en')
    return result.get('Entities')

#create function to detect entity using comprehend
def detect_entity(text):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    result = comprehend.detect_entities(Text=text, LanguageCode='en')
    return result.get('Entities')

# #create function to send the response to S3 bucket
# def send_response_to_s3(response):
#     #convert byte to string
#     response = response
#     s3 = boto3.client('s3', region_name='us-east-1',)
#     s3.put_object(Body=response, Bucket='opensearchdemosanjay', Key='response.txt')

# import boto3

def send_response_to_s3(local_file_path, bucket_name, s3_file_name, region):
    
    s3 = boto3.client('s3',region_name=region)
    try:
        s3.upload_file(local_file_path, bucket_name, s3_file_name)
        print(f"File {local_file_path} uploaded to S3 bucket {bucket_name} as {s3_file_name}")
        
    except Exception as e:
        print(f"Error uploading file: {e}")
    return f"https://{bucket_name}.s3.amazonaws.com/{s3_file_name}"


#create function to convert text to speech using Polly
def text_to_speech(text):
    polly = boto3.client('polly',region_name='us-east-1')
    response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')
    file = open('speech.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()
    return 'speech.mp3'

#create function to convert image to text using textract
def image_to_text(image):
    textract = boto3.client('textract', region_name='us-east-1')
    with open(image, 'rb') as image:
        response = textract.detect_document_text(Document={'Bytes': image.read()})
    text = ''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            text += item['Text'] + ' '
    return text

#create function to convert pdf to text using textract
def pdf_to_text(pdf):
    textract = boto3.client('textract',region_name='us-east-1')
    with open(pdf, 'rb') as pdf:
        response = textract
        response = textract.start_document_text_detection(Document={'Bytes': pdf.read()})
    text = ''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            text += item['Text'] + ' '
    return text

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="500" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display,unsafe_allow_html=True)