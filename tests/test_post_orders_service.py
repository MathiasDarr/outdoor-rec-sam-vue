import boto3
import requests
import json
import time
from test_utilities import authenticate_user, get_order_detail

cf_client = boto3.client('cloudformation')

orders_stack = 'ourdoorrec-orders-api-stack'

response = cf_client.describe_stacks(StackName=orders_stack)
outputs = response["Stacks"][0]["Outputs"]

dynamo_resource = boto3.resource('dynamodb')
orders_table = dynamo_resource.Table('Orders')


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


customer_email = "dakobedbard@gmail.com"
password = '1!ZionTF'
id_token = authenticate_user(cidp, USER_POOL_CLIENT, customer_email, password)
print(id_token)

post_order_url = '{}/orders'.format(OrdersApiProdUrl)
# headers = {'Authorization': id_token}
body = {"customerID":"dakobedbard@gmail.com", "quantities":[1], "products":["boots"], "vendors":["KUHL"]}
presigned_url = '{}/orders'.format(OrdersApiProdUrl)
post_order_response = requests.post(presigned_url, json=body, headers = {'Authorization': "dfd"})

json_response = post_order_response.json()
body = json.loads(json_response['body'])
orderID = body['order']

get_order_detail(orders_table, customer_email, orderID)


body = post_order_response.json()
print(post_order_response.json())












def test_authenticated_user_posts_order():
    post_order_url = '{}/orders'.format(OrdersApiProdUrl)
    # headers = {'Authorization': id_token}
    body = {"customerID": "dakobedbard@gmail.com", "quantities": [1], "products": ["boots"], "vendors": ["KUHL"]}
    presigned_url = '{}/orders'.format(OrdersApiProdUrl)
    lambda_presigned_post = requests.post(presigned_url, json=body, headers={'Authorization': "dfd"})

    assert lambda_presigned_post.status_code == 200
    print(lambda_presigned_post)
