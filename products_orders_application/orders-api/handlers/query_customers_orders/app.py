import json
import boto3
from boto3.dynamodb.conditions import Key
import os
import json
import time
import urllib.request
from jose import jwk, jwt
from jose.utils import base64url_decode


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

TABLE_NAME = 'Orders'
table = dynamo_resource.Table(TABLE_NAME)


def authenticate_identification_token(customerID, token):
    """
    This method
    :param customerID: email of customer
    :param token: token received from cognito authentication
    :return:
    """
    headers = jwt.get_unverified_headers(token)
    kid = headers['kid']
    # search for the kid in the downloaded public keys
    key_index = -1
    for i in range(len(keys)):
        if kid == keys[i]['kid']:
            key_index = i
            break
    if key_index == -1:
        print('Public key not found in jwks.json')

    # construct the public key
    public_key = jwk.construct(keys[key_index])
    # get the last two sections of the token,
    # message and signature (encoded in base64)
    message, encoded_signature = str(token).rsplit('.', 1)
    # decode the signature
    decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))
    # verify the signature
    if not public_key.verify(message.encode("utf8"), decoded_signature):
        print('Signature verification failed')

    print('Signature successfully verified')
    # since we passed the verification, we can now safely
    # use the unverified claims
    claims = jwt.get_unverified_claims(token)

    if time.time() > claims['exp']:
        print('Token is expired')
        return False

    if claims['aud'] != app_client_id or claims['email'] != customerID:
        print('Token was not issued for this audience')
        return False
    return True


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

    token = event['headers']['Authorization']
    customerID = event['pathParameters']['customerID']
    is_authenticated = authenticate_identification_token(customerID,token)

    if not is_authenticated:
        return {"statusCode": 403, "body": json.dumps({
            "error": "Token has expired or been issued to different user."
        }), 'headers': {"Access-Control-Allow-Origin": "*"}}
    else:
        orders = query_orders_by_customer(customerID)
        response = {"statusCode": 200, "body": json.dumps({
            "categories": orders
        }), 'headers': {"Access-Control-Allow-Origin": "*"}}

        return response
