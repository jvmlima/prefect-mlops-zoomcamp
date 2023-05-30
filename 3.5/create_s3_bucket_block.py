from time import sleep
from prefect_aws import S3Bucket, AwsCredentials

import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('config.cfg')

AWS_KEY = config.get('AWS', 'KEY')
AWS_SECRET = config.get('AWS', 'SECRET')

def create_aws_creds_block():
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET
    )
    my_aws_creds_obj.save(name="my-aws-creds", overwrite=True)


def create_s3_bucket_block():
    aws_creds = AwsCredentials.load("my-aws-creds")
    my_s3_bucket_obj = S3Bucket(
        bucket_name="totaleren-mlops-zoomcamp-prefect", credentials=aws_creds
    )
    my_s3_bucket_obj.save(name="totaleren-mlops-zoomcamp-prefect", overwrite=True)


if __name__ == "__main__":
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()
