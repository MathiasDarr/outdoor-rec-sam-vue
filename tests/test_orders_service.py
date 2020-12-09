import boto3
import requests
import json
import time
from test_utilities import authenticate_user


cf_client = boto3.client('cloudformation')

orders_stack = 'ourdoorrec-orders-api-stack'

response = cf_client.describe_stacks(StackName=orders_stack)
outputs = response["Stacks"][0]["Outputs"]

OrdersApiProdUrl = ''

for output in outputs:
    keyName = output["OutputKey"]
    if keyName == "OrdersApi":
        OrdersApiProdUrl = output["OutputValue"]


userpool_stack = 'ourdoorrec-customers-stack'
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

print(OrdersApiProdUrl)
print(USER_POOL_CLIENT)
print(USER_POOL)

cidp = boto3.client('cognito-idp')


def test_authenticated_user_get_orders():
    userID = "dakobedbard@gmail.com"
    password = '1!ZionTF'
    id_token = authenticate_user(cidp, USER_POOL_CLIENT, userID, password)
    return  id_token

test_authenticated_user_get_orders()