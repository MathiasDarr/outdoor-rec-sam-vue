import boto3
import requests
import json
import time


cf_client = boto3.client('cloudformation')

userpool_stack = 'upload-user-stack'
response = cf_client.describe_stacks(StackName=userpool_stack)
outputs = response["Stacks"][0]["Outputs"]

USER_POOL = ''
USER_POOL_CLIENT = ''
for output in outputs:
    keyName = output["OutputKey"]
    if keyName == "UserPool":
        USER_POOL = output["OutputValue"]
    elif keyName == "UserPoolClient":
        USER_POOL_CLIENT = (output["OutputValue"])

upload_api_stack = 'upload-api-stack'
response = cf_client.describe_stacks(StackName=upload_api_stack)
outputs = response["Stacks"][0]["Outputs"]

S3__UPLOAD_BUCKET = ''
GATEWAY_PROD_URL = ''
for output in outputs:
    keyName = output["OutputKey"]
    if keyName == "S3UploadBucket":
        S3__UPLOAD_BUCKET = output["OutputValue"]
    elif keyName == "UploadApi":
        GATEWAY_PROD_URL = (output["OutputValue"])

print(USER_POOL_CLIENT)
print(USER_POOL)
print(GATEWAY_PROD_URL)

cidp = boto3.client('cognito-idp')

dynamodb = boto3.resource('dynamodb', region_name="us-west-2")
user_upload_table = dynamodb.Table('UserUploadTable')

s3_client = boto3.client('s3')



def test_