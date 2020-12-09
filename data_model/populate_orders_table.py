"""
This script reads the orders csv file & populates the orders table.
dynamoDB table.
"""
# !/usr/bin/env python3


import boto3
import csv
from boto.dynamodb.types import Decimal
import os
from time import sleep


def insert_order(order):
    quantities_string = order['quantities'][1:-1]
    quantities = quantities_string.split(',')

    vendors_string = order['vendors'][1:-1]
    vendors = vendors_string.split(',')

    products_string = order['products'][1:-1]
    products = products_string.split(',')


    return table.put_item(
        Item={
            'orderID': order['orderID'],
            'customerID': order['customerID'],
            'vendors': vendors,
            'products': products,
            'order_status': order['order_status'],
            'quantities': [int(q) for q in quantities],
            'total_price': order['total_price']
        }
    )


def create_orders_table():
    try:
        resp = dynamodb.create_table(

            TableName="Orders",

            AttributeDefinitions=[
                {
                    "AttributeName": "customerID",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "orderID",
                    "AttributeType": "S"
                },

            ],

            KeySchema=[
                {
                    "AttributeName": "customerID",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "orderID",
                    "KeyType": "RANGE"
                }
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            },
        )
        return resp
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:4566")
    dynamodb = boto3.resource('dynamodb') #, endpoint_url="http://localhost:8000")
    # create_orders_table()
    # sleep(20)
    table = dynamodb.Table('Orders')

    with open('data/orders.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_order(row)
