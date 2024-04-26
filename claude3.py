
import boto3
import base64
import json
import re
bedrock_runtime = boto3.client('bedrock-runtime',region_name='us-east-1')
from IPython.display import Markdown, display


class Analyticsfunction:
    def __init__(self):
        pass

    def convert_image_to_base64(self, image_path):
        self.image_path = image_path
        with open(self.image_path, "rb") as image_file:
            image_bytes = image_file.read()
            base64_string = base64.b64encode(image_bytes).decode('utf-8')
        return base64_string

    def call_claude_sonet(self, base64_string, question):
        self.question = question
        self.base64_string = base64_string

        prompt_config = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 4096,
                "temperature": 0.0,
                "top_k": 250,
                "top_p": 1,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": base64_string,
                                },
                            },
                            {"type": "text", "text": question},
                        ],
                    }
                ],
            }


        body = json.dumps(prompt_config)
        modelId = "anthropic.claude-3-sonnet-20240229-v1:0"
        accept = "application/json"
        contentType = "application/json"


        response = bedrock_runtime.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
        response_body = json.loads(response.get("body").read())
        results = response_body.get("content")[0].get("text")
        return results
    
    def call_claude_sonet_text(self, question):
        self.question = question
        prompt_config = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 700,
                "temperature": 0.9,
                "top_k": 250,
                "top_p": 0.9,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                        
                            {"type": "text", 
                             "text": question},
                        ],
                    }
                ],
            }


        body = json.dumps(prompt_config)
        modelId = "anthropic.claude-3-sonnet-20240229-v1:0"
        accept = "application/json"
        contentType = "application/json"


        response = bedrock_runtime.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
        response_body = json.loads(response.get("body").read())
        results = response_body.get("content")[0].get("text")
        #out = display(Markdown(results))
        return results
    
    
    
    import re

def extract_python_code(input_text, output_file):
    # Regular expression pattern to match Python code blocks
    python_pattern = r'```python\n(.*?)```'
    # Find all Python code blocks using regex
    python_blocks = re.findall(python_pattern, input_text, re.DOTALL)
    # Write Python code blocks to the output file
    with open(output_file, 'w') as f:
        for code_block in python_blocks:
            f.write(code_block.strip() + '\n\n')

            
def detect_shape(question):
    prompt = f'''Human: find out the math image shape from question
    some example of question and asnwer is given below
    if there the two word in shape then add  underscore
    question = "ABCDEF is a hexagon (six-sided polygon). Find the value of AB+BC+CD+DE+AF+FE+AE "
    answer = "hexagom"
    
    question = "If the adjacent sides of a parallelogram are 3i+2j and -i+4j+2k, find the area of the   parallelogram."
    answer = "parallelogram"
    

    <question>
    {question}
    </question>
    please answer only the type of shape

    Assistant:'''

    text = claude3(prompt) 
    return text