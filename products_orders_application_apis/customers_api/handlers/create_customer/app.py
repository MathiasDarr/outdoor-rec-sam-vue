import json
import boto3
from boto3.dynamodb.conditions import Key
import os
import json
import time
import urllib.request



region = os.getenv('region')
userpool_id = os.getenv('userpool_id')
app_client_id = os.getenv('app_client_id')
keys_url = 'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(region, userpool_id)


with urllib.request.urlopen(keys_url) as f:
    response = f.read()
keys = json.loads(response.decode('utf-8'))['keys']

dynamo_endpoint = os.getenv('dynamo_endpoint')
if dynamo_endpoint == 'cloud':
    dynamo_resource = boto3.resource('dynamodb')
else:
    dynamo_resource = boto3.resource('dynamodb', endpoint_url=dynamo_endpoint)

TABLE_NAME = 'Customers'
table = dynamo_resource.Table(TABLE_NAME)


def insert_customer(customer):
    response = table.put_item(
        Item={
            'first_name': customer['first_name'],
            'last_name': customer['last_name'],
            'customerID': customer['customerID'],
            'verified': False
        }
    )
    return response


def lambda_handler(event, context):
    """

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    body = json.loads(event['body'])

    customer = {}
    customer['customerID'] = event['pathParameters']['customerID']
    customer['first_name'] = body['first_name']
    customer['last_name'] = body['last_name']

    insert_response = insert_customer(customer)

    response = {"statusCode": 200, "body": json.dumps({
        "categories": insert_response
    }), 'headers': {"Access-Control-Allow-Origin": "*"}}

    return response
