#!/bin/bash

aws dynamodb scan --table Products --endpoint-url http://localhost:8000
aws dynamodb scan --table Categories --endpoint-url http://localhost:8000
