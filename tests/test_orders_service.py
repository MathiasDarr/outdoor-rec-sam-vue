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

def test_unauthenticated_orders_query_request_returns_403():
    orders_query_url = '{}/orders'.format(OrdersApiProdUrl)
    headers = {'Authorization': 'not a token'}
    get_orders_response = requests.get(orders_query_url) #, headers = headers)
    return get_orders_response
    #assert get_orders_response.status_code == 403

resp = test_unauthenticated_orders_query_request_returns_403()

def test_authenticated_user_get_orders():
    userID = "dakobedbard@gmail.com"
    password = '1!ZionTF'
    id_token = authenticate_user(cidp, USER_POOL_CLIENT, userID, password)

    orders_query_url = '{}/orders'.format(OrdersApiProdUrl)
    headers = {'Authorization': id_token}

    get_orders_response = requests.get(orders_query_url, headers = headers)
    assert get_orders_response.status_code == 200

    json_response = get_orders_response.json()
    orders = json.loads(json_response['body'])['orders']
    assert all([order['customerID'] == userID for order in orders])


# userID = "dakobedbard@gmail.com"
# orders = test_authenticated_user_get_orders()
# assert all([order['customerID'] == userID for order in orders])
#
# print(get_orders_response.json())

userID = "dakobedbard@gmail.com"
password = '1!ZionTF'
id_token = authenticate_user(cidp, USER_POOL_CLIENT, userID, password)
print(id_token)