import json
import boto3
from boto3.dynamodb.conditions import Key
import os

dynamo_endpoint = os.getenv('dynamo_endpoint')
if dynamo_endpoint == 'cloud':
    dynamo_resource = boto3.resource('dynamodb')
else:
    dynamo_resource = boto3.resource('dynamodb', endpoint_url=dynamo_endpoint)

TABLE_NAME = 'Orders'
table = dynamo_resource.Table(TABLE_NAME)


def query_orders_by_customer(customer):
    orders = table.query(
        KeyConditionExpression=Key('customerID').eq(customer)
    )
    orders = orders['Items']
    return orders


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
    # vendor = event['pathParams']['vendor']
    customerID = event['pathParameters']['customerID']
    orders = query_orders_by_customer(customerID)

    response = {"statusCode": 200, "body": json.dumps({
        "categories": orders
    }), 'headers': {"Access-Control-Allow-Origin": "*"}}

    return response
