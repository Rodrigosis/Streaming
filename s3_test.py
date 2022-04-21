import uuid
import boto3
import os
from dotenv import load_dotenv

load_dotenv()
# print(uuid.uuid4())


session = boto3.Session(aws_access_key_id=os.getenv('AWSAccessKeyId'),
                        aws_secret_access_key=os.getenv('AWSSecretKey'))

s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)


if __name__ == '__main__':
    pass
