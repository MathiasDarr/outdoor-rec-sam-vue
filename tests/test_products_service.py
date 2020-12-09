import boto3
import requests
import json
import time

cf_client = boto3.client('cloudformation')

products_stack = 'ourdoorrec-products-api-stack'
response = cf_client.describe_stacks(StackName=products_stack)
outputs = response["Stacks"][0]["Outputs"]

ProductsApiProdUrl = ''

for output in outputs:
    keyName = output["OutputKey"]
    if keyName == "ProductsApi":
        ProductsApiProdUrl = output["OutputValue"]

print(ProductsApiProdUrl)


def test_query_products_by_vendor():
    """
    Test querying products by vendor and asserting that all returned products are of the same vendor
    :return:
    """
    vendor = 'KUHL'
    query_url = '{}/products/vendor/{}'.format(ProductsApiProdUrl, vendor)
    query_response = requests.get(query_url)
    body = json.loads(query_response.json()['body'])
    assert all([product['vendor'] == vendor for product in body['products']])


def test_query_products_by_category():
    """
    Test querying products by category and asserting that all returned products are of the correct category
    :return:
    """
    category = 'mens-boots'
    query_url = '{}/products/category/{}'.format(ProductsApiProdUrl, category)
    query_response = requests.get(query_url)
    body = json.loads(query_response.json()['body'])
    assert all([product['category'] == category for product in body['products']])
