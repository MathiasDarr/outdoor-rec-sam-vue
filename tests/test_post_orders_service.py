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


def test_unauthenticated_user_posts_order():
    """
    Submit post request to the ordres route w/out a valid Authorization header
    :return:
    """
    products = ["boots"]
    vendors = ["KUHL"]
    quantities = [1]
    body = {"quantities": quantities, "products": products, "vendors": vendors}
    post_order_url = '{}/orders'.format(OrdersApiProdUrl)
    post_order_response = requests.post(post_order_url, json=body, headers={'Authorization': "dfd"})
    assert post_order_response.status_code == 403

test_unauthenticated_user_posts_order()


def test_authenticated_user_posts_order():
    customer_email = "dakobedbard@gmail.com"
    password = '1!ZionTF'
    id_token = authenticate_user(cidp, USER_POOL_CLIENT, customer_email, password)

    headers = {'Authorization': id_token}

    products = ["boots"]
    vendors = ["KUHL"]
    quantities = [1]
    body = {"customerID": customer_email, "quantities": quantities, "products": products, "vendors": vendors}
    post_order_url = '{}/orders'.format(OrdersApiProdUrl)
    post_order_response = requests.post(post_order_url, json=body, headers=headers)

    assert post_order_response.status_code == 200

    json_response = post_order_response.json()
    body = json.loads(json_response['body'])

    orderID = body['order']

    order = get_order_detail(orders_table, customer_email, orderID)

    response_products = order['products']
    response_quantities = order['quantities']
    response_vendors = order['vendors']
    response_customer_email = order['customerID']

    assert products == response_products
    assert vendors == response_vendors
    assert customer_email == response_customer_email
    assert quantities == response_quantities

test_authenticated_user_posts_order()
