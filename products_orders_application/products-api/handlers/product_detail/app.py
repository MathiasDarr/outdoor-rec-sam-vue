"""
The lambda function defined here queries the category GSI

"""

import json
import boto3
from boto3.dynamodb.conditions import Key
import os


dynamo_endpoint = os.getenv('dynamo_endpoint')
if dynamo_endpoint == 'cloud' or dynamo_endpoint =='':
    dynamo = boto3.client('dynamodb')
else:
    dynamo = boto3.client('dynamodb',endpoint_url=dynamo_endpoint)

TABLE_NAME = 'Products'


def get_product_detail(vendor, product_name):
    response = dynamo.get_item(
        TableName=TABLE_NAME,
        Key={
            'vendor': {'S': vendor},
            'productName': {'S': product_name}
        }
    )
    return response['Item']


product_name = 'Heeled Boots'
vendor ="Blundstone"
get_product_detail(vendor, product_name)



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

    vendor = event['pathParameters']['vendor']
    productName = event['pathParameters']['productName']
    productName = productName.replace('%20', ' ')
    product = get_product_detail(vendor, productName)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "product": product,
            'headers': {"Access-Control-Allow-Origin": "*"}
        }),
    }
