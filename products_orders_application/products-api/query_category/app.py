"""
The lambda function defined here queries the category GSI

"""

import json
import boto3
from boto3.dynamodb.conditions import Key
import os


dynamo_endpoint = os.getenv('dynamo_endpoint')
if dynamo_endpoint == 'cloud':
    dynamo_resource = boto3.resource('dynamodb')
else:
    dynamo_resource = boto3.resource('dynamodb',endpoint_url=dynamo_endpoint)

TABLE_NAME = 'Products'
table = dynamo_resource.Table(TABLE_NAME)


def query_products_by_category(category):
    response = table.query(
        # Add the name of the index you want to use in your query.
        IndexName="categoryGSI",
        KeyConditionExpression=Key('category').eq(category),
    )
    products = response['Items']
    for product in products:
        product['price'] = float(product['price'])
    return products


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

    category = event['pathParameters']['category']
    products = query_products_by_category(category)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "products": products,
            # "type": str(event.keys())
            # "location": ip.text.replace("\n", "")
        }),
    }
