#!/bin/bash

sam local start-api --docker-network local-api-network --parater-overrides DynamoEndpoint=http://dynamo-local:8000