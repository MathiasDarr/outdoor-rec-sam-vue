### Products Orders SAM Application ###

* products-api
    - API for querying the products database
    - Lambda function for querying by partition key, in this case vendor/brand i.e 'North Face'
    - Lambda function for querying the global secondary index (category being the partition key) i.e 'mens-boots'
* orders-api
    - API enables authenticated users (AWS Cognito) to perform CRUD operations on an orders DynamoDB table    

    
### This Application Has the Following Dependencies ###
* AWS SAM
* boto3
* docker & docker-compose (if testing w/ localstack)
    
### Running the Application Locally ### 

        
* run the products query api locally
    - cd products-api
    - sam local start-api
    - query all Patagonia products
        - curl http://localhost:3000/products/vendor/Patagonia
    - query the category GSI for all mens boots 
        - curl http://localhost:3000/products/category/mens-boots
### Deploying the Application to AWS ###
* deploy to AWS cloud 
    - cd products-api
    
### Run Tests ###
* pytest