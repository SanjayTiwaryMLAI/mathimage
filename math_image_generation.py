# importing required modules 

import streamlit as st

import components.authenticate as authenticate
st.set_page_config(page_title="Math Image Generation Demo using LLM Chaining", layout="wide")
st.title(" 🔗 Math Image Generation Demo using LLM Chaining")
st.write("🧑 Developed by Sanjay- AWS")
# Check authentication
authenticate.set_st_state_vars()

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()


if (
    st.session_state["authenticated"]
    and "adminaccess" in st.session_state["user_cognito_groups"]
):

    
    import boto3
    import os
    import json
    import time
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    from core_lib.math_question_generation import Analyticsfunction, mathquestion
    from PIL import Image
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    s3 = boto3.client('s3')
    
    # Global variable to store the summary
    summary = ""
    
    # Define table names
    table_name_math_question = 'mathquestion_image'
    table_name_question_answer = 'question_answer'
    table_name_summarization = 'summarization'
    bucket_name = 'document-tender'
    
    # Initialize DynamoDB tables
    def initialize_tables():
        # Math Question and Image table
        table = dynamodb.Table(table_name_math_question)
        try:
            table.table_status
        except:
            table = dynamodb.create_table(
                TableName=table_name_math_question,
                KeySchema=[
                    {
                        'AttributeName': 'question',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'image_url',
                        'KeyType': 'RANGE'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'question',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'image_url',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            print(f"Table '{table_name_math_question}' created successfully!")
        else:
            print(f"Table '{table_name_math_question}' already exists.")
    
        # Question and Answer table
        table = dynamodb.Table(table_name_question_answer)
        try:
            table.table_status
        except:
            table = dynamodb.create_table(
                TableName=table_name_question_answer,
                KeySchema=[
                    {
                        'AttributeName': 'question',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'question',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            print(f"Table '{table_name_question_answer}' created successfully!")
        else:
            print(f"Table '{table_name_question_answer}' already exists.")
    
        # Summarization table
        table = dynamodb.Table(table_name_summarization)
        try:
            table.table_status
        except:
            table = dynamodb.create_table(
                TableName=table_name_summarization,
                KeySchema=[
                    {
                        'AttributeName': 'summary',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'summary',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            print(f"Table '{table_name_summarization}' created successfully!")
        else:
            print(f"Table '{table_name_summarization}' already exists.")
    
    #initialize_tables()
    # @st.cache_data
    math = mathquestion()
    def create_image1(question):
        math = mathquestion()
    
        prompt = f'''Human: Please create a Python script to generate an informative and visually appealing image representing the mathematical concept or problem: {question}
                        Please follow these guidelines:
                        1. Use the seaborn package to create the plot, and save it as "image.jpg" with a resolution of 100 dpi.
                        2. Ensure the code must be complete in all aspect
                        3. Ensure the image covers approximately 80% of the area, leaving space for labels.
                        4. Complete all edges and align them properly for the chosen shape or representation.
                        5. Label relevant components (e.g., edges, vertices, angles) with clear annotations for better understanding.
                        6. Import all necessary libraries and functions required for the task.
                        7. The code should be accurate, well-structured, and easy to understand.
                        8. Consider using color, shading, and other visual elements to enhance the clarity and aesthetics of the image.
                        9. check the correctness of python code and made sure library imports are proper.
    
    
                        Assistant:'''
        
    
        body = json.dumps({"prompt": prompt})
        text = math.call_claude_sonet_text_35(body)
        
        
        return text
        
    def create_image(question):
        text = create_image1(question)
       
        prompt2 = f'''Human: Your task is Check the correctness and review the the Python code /n {text} and make sure no library import is missing,rewrite the updated code but don't change the important section of the code.
                Assistant:'''
                
        body2 = json.dumps({"prompt": prompt2})
        text2 = math.call_claude_sonet_text(body2)
        
        st.write(text2)
        
        image_name = "image.jpg"
        output_file = "main.py"
        new = math.extract_python_code(text2, output_file)
        with open("main.py", "r") as file:
            script_contents = file.read()

        # Display the script contents
        st.write("Contents of script.py:")
        st.code(script_contents, language="python")
        
        # time.sleep(3)
        os.system(f"python3 {output_file}")
    
        # Check if the image file exists
        if os.path.isfile(image_name):
            #img = mpimg.imread(image_name)
            img = Image.open(image_name)
            #st.image(img, width=400)
            bucket_name = 'document-tender'
            # Upload image to S3 bucket
            s3.upload_file(image_name, bucket_name, image_name)
            image_url = f"https://{bucket_name}.s3.amazonaws.com/{image_name}"
    
            # Save image URL to DynamoDB
            table = dynamodb.Table(table_name_math_question)
            response = table.put_item(
                Item={
                    'question': question,
                    'image_url': image_url
                }
            )
            #st.write(f"Image URL saved to DynamoDB: {response['ResponseMetadata']['HTTPStatusCode']}")
    
        else:
            st.write(f"Error: Image file '{image_name}' not found.")
    
        return img
    
    
    # Function to translate text
    @st.cache_resource
    def translate(text, source_lang='en', target_lang='hi'):
        translate = boto3.client(service_name='translate', region_name='us-east-1')
        result = translate.translate_text(Text=text, SourceLanguageCode=source_lang, TargetLanguageCode=target_lang)
        return result.get('TranslatedText')
    
    # Function to extract JSON data
    # @st.cache_data
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
    
    num_questions = st.number_input("Enter the number of questions to generate", min_value=2, max_value=10, value=2)
    
    # Ask question button
    question = st.text_input("Enter your question:")
    ask_question_button = st.button("Ask Question")
    
    if ask_question_button:

        img = create_image(question)
        st.image(img, width=400)
        
        
    
    st.markdown("<h1 style='font-size: 20px; color: blue;'>Upload Input Text 📥</h1>", unsafe_allow_html=True)
    
    input_text = st.file_uploader("Upload a text file 📂", type=["txt"])
    
    if input_text is not None:
        # Summarization ✂️
        start_summarization = st.button("Start Summarization 🚀")
        if start_summarization:
            st.markdown("<h1 style='font-size: 20px; color: blue;'>Text Summarization 📝</h1>", unsafe_allow_html=True)
            text = input_text.read().decode('utf-8')
            obj = Analyticsfunction()
            claude3 = obj.call_claude_sonet_text
            math = mathquestion()
            summary = math.create_summary(text)
            new_summary = translate(summary, target_lang=selected_lang)
            st.write(translate(summary, target_lang=selected_lang))
    
            # Save summary to local file
            with open('summary.txt', 'w') as f:
                f.write(new_summary)
    
            # Upload summary to S3 bucket
            bucket_name = 'document-tender'
            s3.upload_file('summary.txt', bucket_name, 'summary.txt')
            summary_url = f"https://{bucket_name}.s3.amazonaws.com/summary.txt"
    
            # Save summary URL to DynamoDB
            table = dynamodb.Table(table_name_summarization)
            response = table.put_item(
                Item={
                    'summary': summary_url
                }
            )
            #st.write(f"Summary URL saved to DynamoDB: {response['ResponseMetadata']['HTTPStatusCode']}")
    
        # Q&A ❓
        start_qa = st.button("Start Question & Answer 🤔")
        math = mathquestion()
        with open('summary.txt', 'r') as f:
            summary = f.read()
        if start_qa:
            st.markdown("<h1 style='font-size: 20px; color: blue;'>Question & Answer ❓❔</h1>", unsafe_allow_html=True)
    
            prompt = f'''Human: Please generate {num_questions} number of multiple-choice question and their respective answers based on the content provided in the attached document. The questions should cover a range of difficulty levels (easy, medium, and hard) and test different aspects of the content, such as factual information, concepts, and analysis. Each question should have 4 answer choices, with only one correct answer. Please include question, options, answer, and explanation. 
                <book>
                {summary}
                </book>
                Please create the response in JSON format.
    
                Assistant:'''
            body = json.dumps({"prompt": prompt})
            question = math.question_answer_generation(body)
            
            json_data = extract_json(question)
    
            # Save question, answer, and explanation to DynamoDB
            table = dynamodb.Table(table_name_question_answer)
            for question_data in json_data["questions"]:
                response = table.put_item(
                    Item={
                        'question': question_data['question'],
                        'answer': question_data['answer'],
                        'options': question_data['options'],
                        'explanation': question_data['explanation']
                    }
                )
            
            #st.write(f"Question data saved to DynamoDB: {response['ResponseMetadata']['HTTPStatusCode']}")
    
            # Parse JSON data and display on UI
            #st.write(json_data)
            i = 1
            for question in json_data["questions"]:
                #add spinner
                # with st.spinner("Wait for it..."):
                #         time.sleep(1)
                st.write(f"**Question ({i})**: {translate(question['question'], target_lang=selected_lang)}")
                img = create_image(question["question"])
                st.image(img, width=400)
                # time.sleep(4)
                st.write(f"**Options**: {question['options']}")
                st.write(f"**Answer**: {question['answer']} ")
                st.write(f"**Explanation**: {translate(question['explanation'], target_lang=selected_lang)} 💡")
                st.write("--------------------------------------")
                i += 1
                time.sleep(2)
      
    
    # Run the app
    if __name__ == "__main__":
        st.sidebar.markdown("""
        <large>Created by Anthropic's Claude 3 Sonnet using Bedrock</large>
        """, unsafe_allow_html=True)
        st.sidebar.markdown("""
        <large>Using chain of thought (COT)</large>
        """, unsafe_allow_html=True)
        st.sidebar.markdown("""
        <small>Note: This app requires an active internet connection and may take some time to load.</small>
        """, unsafe_allow_html=True)
        st.sidebar.markdown("<h1 style='font-size: 16px; color: black;'>Question1 : ABCDEF is a hexagon (six-sided polygon). Find the value of AB+BC+CD+DE+AF+FE+AE ?</h1>", unsafe_allow_html=True)
        st.sidebar.markdown("<h1 style='font-size: 16px; color: black;'>Question2: If the position vectors of the vertices A, B, and C of a triangle △ABC are αi+βj+γk, βi+γj+αk, and γi+αj+βk respectively, then △ABC is ?</h1>", unsafe_allow_html=True)
        st.sidebar.markdown("<h1 style='font-size: 16px; color: black;'>Question3: what is area of rectangle?</h1>", unsafe_allow_html=True)
        st.stop()

else:
    if st.session_state["authenticated"]:
        st.write("You do not have access. Please contact the administrator.")
    else:
        st.write("Please login!")

