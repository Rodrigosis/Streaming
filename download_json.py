import boto3
import os
from dotenv import load_dotenv

load_dotenv()


session = boto3.Session(aws_access_key_id=os.getenv('AWSAccessKeyId'),
                        aws_secret_access_key=os.getenv('AWSSecretKey'))

s3 = session.resource('s3')
bucket = s3.Bucket('main-streaming')

for n in range(1, 1000):
    str_int = str(n)

    while len(str_int) < 5:
        str_int = '0' + str_int

    try:
        bucket.download_file(f'{str_int}/{str_int}.json', f'json/{str_int}.json')
    except Exception as e:
        print(e)
        break

if __name__ == '__main__':
    pass
