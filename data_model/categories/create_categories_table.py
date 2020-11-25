"""
This script create the categories dynamo table
"""
# !/usr/bin/env python3
import boto3
from time import sleep


def create_categories_table():
    try:
        dynamodb.create_table(
            AttributeDefinitions=[
                {
                    "AttributeName": "category",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "subcategory",
                    "AttributeType": "S"
                },
            ],
            TableName='Categories',
            KeySchema=[
                {
                    "AttributeName": "category",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "subcategory",
                    "KeyType": "RANGE"
                }
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            },
        )

    except Exception as e:
        print(e)


if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')

    create_categories_table()
    sleep(2)

    table = dynamodb.Table('Categories')

    categories = [('mens-boots', 'boots', 'M'),('day-packs', 'backpacks', 'womens-running-jackets', 'jackets','W') , ('womens-rain-jackets', 'jackets', 'w'),
                   ('womens-insulated-jackets','jackets','W'), ('womens-fleece-and-soft-shell-jackets', 'jackets','W', 'womens-casual-jackets', 'jackets', 'W'),
                   ('womens-boots', 'boots', 'W'), ('mens-winter-boots','boots','M'), ('mens-snow-jackets', 'jackets','M'), ('mens-running-jackets', 'jackets', 'M'),
                   ('mens-rain-jackets', 'jackets', 'M'), ('mens-insulated-jackets','jackets','M' ), ('mens-fleece-and-soft-shell-jackets','jackets','M'),
                   ('mens-casual-jackets', 'jackets','M')
                   ]

    for category in categories:
        table.put_item(
            Item={
                'category': category[0],
                'subcategory': category[1],
                'gender':category[2]
            }
        )
