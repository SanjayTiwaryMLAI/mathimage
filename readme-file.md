# Math Image Generation Demo using LLM Chaining

This Streamlit application demonstrates math image generation using Large Language Model (LLM) chaining. It allows users to generate math questions, create corresponding images, and perform question-answering tasks.

## Features

- User authentication using Cognito
- Math question generation
- Image creation for math questions
- Text summarization
- Question and answer generation
- Multi-language support

## Installation

1. Clone this repository
2. Install the required packages:

```
pip install -r requirements.txt
```

3. Set up your AWS credentials and ensure you have the necessary permissions for DynamoDB, S3, and other AWS services used in this application.

## Usage

Run the Streamlit app:

```
streamlit run app.py
```

## Configuration

Ensure you have the following environment variables set:

- AWS credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
- Cognito User Pool settings
- DynamoDB table names
- S3 bucket name

## Dependencies

See `requirements.txt` for a full list of dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
