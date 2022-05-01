import boto3
import os
from dotenv import load_dotenv

load_dotenv()

json_name = '00001'
session = boto3.Session(aws_access_key_id=os.getenv('AWSAccessKeyId'),
                        aws_secret_access_key=os.getenv('AWSSecretKey'))

s3 = session.resource('s3')

s3.meta.client.upload_file(Filename=f'json/{json_name}.json', Bucket='main-streaming', Key=f'{json_name}/{json_name}.json')

if __name__ == '__main__':
    pass
