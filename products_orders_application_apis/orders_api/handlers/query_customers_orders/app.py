import logging
import boto3
from botocore.exceptions import ClientError
import os
import time
import urllib.request
from jose import jwk, jwt
from jose.utils import base64url_decode
import json
from boto3.dynamodb.conditions import Key


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




def verify_identification_token(token):
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

    if claims['aud'] != app_client_id:  # or claims['email'] != customerID:
        print('Token was not issued for this audience')
        return False
    return claims['email']


def create_presigned_post(bucket_name, object_name, fields=None, conditions=None, expiration=3600):
    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3', region_name='us-west-2')
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL and required fields
    return response


def query_orders_by_customer(customer):
    orders = table.query(
        KeyConditionExpression=Key('customerID').eq(customer)
    )
    orders = orders['Items']
    for order in orders:
        order['total_price'] = float(order['total_price'])
        quantities_list = [int(quantity) for quantity in order['quantities']]
        order['quantities'] = quantities_list

    return orders

def lambda_handler(event, context):
    if 'Authorization' not in event['params']['header'] or not verify_identification_token(
            event['params']['header']['Authorization']):
        return {"statusCode": 403, "body": json.dumps({
            "errorMessage": "failure"
        }), 'headers': {"Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}}

    userID = verify_identification_token(event['params']['header']['Authorization'])

    orders = query_orders_by_customer(userID)
    # user_upload_directory = get_user_upload_directory(userID)
    # filename = event['body']['filename']
    # presigned = create_presigned_post(BUCKET, '{}/{}'.format(user_upload_directory, filename))
    #
    # presigned['fields']['bucket'] = BUCKET

    response = {"statusCode": 200, "body": json.dumps({
        "presigned": orders
    }), 'headers': {"Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}}
    return response

    # response = {"statusCode": 200, "body": json.dumps({
    #     "presigned": "hello"
    # }), 'headers': {"Access-Control-Allow-Origin": "*", "Content-Type":"application/json"}}
    #
    # return response

    # # print("header")
    # # print((event['params']['header']['Authorization'])
    # if 'Authorization' not in event['params']['header'] or not verify_identification_token(
    #         event['params']['header']['Authorization']):
    #     return {"statusCode": 403, "body": json.dumps({
    #         "errorMessage": "failure"
    #     }), 'headers': {"Access-Control-Allow-Origin": "*", "Content-Type":"application/json"}}
    #
    # userID = verify_identification_token(event['params']['header']['Authorization'])
    #
    # user_upload_directory = get_user_upload_directory(userID)
    # filename = event['body']['filename']
    # presigned = create_presigned_post(BUCKET, '{}/{}'.format(user_upload_directory, filename))
    #
    # presigned['fields']['bucket'] = BUCKET
    #
    # response = {"statusCode": 200, "body": json.dumps({
    #     "presigned": presigned
    # }), 'headers': {"Access-Control-Allow-Origin": "*"}, "Content-Type":"application/json"}
    #
    # return response


# #set($inputRoot = $input.path('$.errorMessage'))
# $inputRoot
#
#
# #set($inputRoot = $input.path('$')) {
#     "error": "$inputRoot.errorMessage"
# }


    # print("header")
    # print((event['params']['header']['Authorization'])
    # if 'Authorization' not in event['params']['header'] or not verify_identification_token(
    #         event['params']['header']['Authorization']):
    #     return {"statusCode": 403, "body": json.dumps({
    #         "errorMessage": "failure"
    #     }), 'headers': {"Access-Control-Allow-Origin": "*", "Content-Type":"application/json"}}
    #
    # userID = verify_identification_token(event['params']['header']['Authorization'])
    #
    # user_upload_directory = get_user_upload_directory(userID)
    # filename = event['body']['filename']
    # presigned = create_presigned_post(BUCKET, '{}/{}'.format(user_upload_directory, filename))
    #
    # presigned['fields']['bucket'] = BUCKET
    #
    # response = {"statusCode": 200, "body": json.dumps({
    #     "presigned": presigned
    # }), 'headers': {"Access-Control-Allow-Origin": "*", "Content-Type":"application/json"}}


# import json
# import boto3
# from boto3.dynamodb.conditions import Key
# import os
# import json
# import time
# import urllib.request
# from jose import jwk, jwt
# from jose.utils import base64url_decode
#
#
# region = os.getenv('region')
# userpool_id = os.getenv('userpool_id')
# app_client_id = os.getenv('app_client_id')
# keys_url = 'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(region, userpool_id)
#
# with urllib.request.urlopen(keys_url) as f:
#   response = f.read()
# keys = json.loads(response.decode('utf-8'))['keys']
#
# dynamo_endpoint = os.getenv('dynamo_endpoint')
# if dynamo_endpoint == 'cloud':
#     dynamo_resource = boto3.resource('dynamodb')
# else:
#     dynamo_resource = boto3.resource('dynamodb', endpoint_url=dynamo_endpoint)
#
# TABLE_NAME = 'Orders'
# table = dynamo_resource.Table(TABLE_NAME)
#
#
# def verify_identification_token(token):
#     """
#     This method
#     :param customerID: email of customer
#     :param token: token received from cognito authentication
#     :return:
#     """
#     headers = jwt.get_unverified_headers(token)
#     kid = headers['kid']
#     # search for the kid in the downloaded public keys
#     key_index = -1
#     for i in range(len(keys)):
#         if kid == keys[i]['kid']:
#             key_index = i
#             break
#     if key_index == -1:
#         print('Public key not found in jwks.json')
#
#     # construct the public key
#     public_key = jwk.construct(keys[key_index])
#     # get the last two sections of the token,
#     # message and signature (encoded in base64)
#     message, encoded_signature = str(token).rsplit('.', 1)
#     # decode the signature
#     decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))
#     # verify the signature
#     if not public_key.verify(message.encode("utf8"), decoded_signature):
#         print('Signature verification failed')
#
#     print('Signature successfully verified')
#     # since we passed the verification, we can now safely
#     # use the unverified claims
#     claims = jwt.get_unverified_claims(token)
#
#     if time.time() > claims['exp']:
#         print('Token is expired')
#         return False
#
#     if claims['aud'] != app_client_id:  # or claims['email'] != customerID:
#         print('Token was not issued for this audience')
#         return False
#     return claims['email']
#
#
# def query_orders_by_customer(customer):
#     orders = table.query(
#         KeyConditionExpression=Key('customerID').eq(customer)
#     )
#     orders = orders['Items']
#     for order in orders:
#         order['total_price'] = float(order['total_price'])
#         quantities_list = [int(quantity) for quantity in order['quantities']]
#         order['quantities'] = quantities_list
#
#     return orders
#
#
# def lambda_handler(event, context):
#     """
#
#     Parameters
#     ----------
#     event: dict, required
#         API Gateway Lambda Proxy Input Format
#
#         Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
#
#     context: object, required
#         Lambda Context runtime methods and attributes
#
#         Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
#
#     Returns
#     ------
#     API Gateway Lambda Proxy Output Format: dict
#
#         Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
#     """
#
#     if 'Authorization' not in event['multiValueHeaders'] or not verify_identification_token(event['multiValueHeaders']['Authorization']):
#         return {"statusCode": 403, "body": json.dumps({
#             "errorMessage": "failure"
#         }), 'headers': {"Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}}
#
#     token = event['multiValueHeaders']['Authorization']
#     user_email = verify_identification_token(token)
#
#     orders = query_orders_by_customer(user_email)
#     response = {"statusCode": 200, "body": json.dumps({
#             "orders": orders
#     }), 'headers': {"Access-Control-Allow-Origin": "*"}}
#
#     return response
