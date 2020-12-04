"""
This script reads the customers csv file & populates the customers table.
dynamoDB table.
"""
# !/usr/bin/env python3


import boto3
import csv
import os
from time import sleep


def insert_customer(order):
    return table.put_item(
        Item={
            'customerID': order['customerID'],
            'first_name': order['first_name'],
            'last_name': order['last_name'],
            'verified': True,
            'primary_address': order['primary_address'],
        }
    )


def create_customer_table():
    try:
        resp = dynamodb.create_table(

            TableName="Customers",

            AttributeDefinitions=[
                {
                    "AttributeName": "customerID",
                    "AttributeType": "S"
                },

            ],

            KeySchema=[
                {
                    "AttributeName": "customerID",
                    "KeyType": "HASH"
                },

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
    #create_customer_table()
    #sleep(15)
    table = dynamodb.Table('Customers')

    with open('data/customers.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_customer(row)
