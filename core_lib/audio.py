# Import library
import boto3
import requests
import textwrap
import uuid

# Set up the Transcribe client
transcribe = boto3.client('transcribe')
wrapper = textwrap.TextWrapper(width=100) 
uuid = uuid.uuid4()
s3 = boto3.client('s3')
#create a list of file from the S3 bucket
#objs = s3.list_objects(Bucket="audiofilessample")['Contents']
#create a function for extracting file name
def get_file_name(path):
    return path.split('/')[-1].split('.')[0]


# create class to convert audio to text
class AudioToText:
    def __init__(self):
        pass

    def convert(self, bucket):

        self.bucket = "audiofilessample"
        objs = s3.list_objects(Bucket=self.bucket)['Contents']
        for obj in objs:
            key = obj['Key']
            bucket = "audiofilessample"
            url = f'https://{bucket}.s3.amazonaws.com/{key}'

            job_name = get_file_name(key)
            job_name = f'{job_name}-{uuid}'
            response = transcribe.start_transcription_job(
                TranscriptionJobName=job_name,
                Media={'MediaFileUri': url},
                IdentifyLanguage = True,
                MediaFormat='mp3'
                #LanguageCode='en-US'
            )
            # Print transcribed text when job is completed
            while True:
                status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
                if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                    break

            text = requests.get(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
            word_list = wrapper.wrap(text.json()['results']['transcripts'][0]['transcript'])
            for element in word_list:
                print(element)
        

