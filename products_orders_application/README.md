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


IdToken: "eyJraWQiOiJpWFVZQXVWdW1RXC9qZ3RJemg1alNKM3V0dEVxU0JnQ1BibnZWbGRrS0tLdz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlNTJkNzhlNy0zMTBiLTQwYzItODAwNy1kNDZlN2E4ZTU1ZjQiLCJhdWQiOiI3Z2NjNmpwN2VubzNmNHZhYWM0M3NyY2lraiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJldmVudF9pZCI6IjIzODczOWI5LTA2MTQtNDdlZi04YTgyLThhY2VkMzczZmRiNSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjA2NzIxNzcyLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl9Fa2d5cmUydEEiLCJjb2duaXRvOnVzZXJuYW1lIjoiZTUyZDc4ZTctMzEwYi00MGMyLTgwMDctZDQ2ZTdhOGU1NWY0IiwiZXhwIjoxNjA2NzI1MzcyLCJpYXQiOjE2MDY3MjE3NzIsImVtYWlsIjoiZGFrb2JlZGJhcmRAZ21haWwuY29tIn0.o3LAG-pGhkSl08ve4AdgTi5niiKnQLP8CyqiucxapzcRoHz1eVTHDdBz_-Cd7kFcdoVm_qGHexC6u0lV7CAUqInSOXoNlea9diMrp7Iw3AmvXICpgtr8EkXelziyVvR7deeedQiD-XCBizqntyYY240vhj6vebbYBz8Z34EdZxgSB-TkqK1JBfH-YzLVHcetQdu0wydpDPtw43E-bUh4j0d2DZ5bcRKmabM11RCVwjagwX6cW3_HubsISsKCDzMyDIyJuMbtkuasTVDmtIPZo1mniNI8-iUqsVhpKhZghtnim6z5t3Ds0TiibfDmKcsAIp6ywZJzXuv57bh4HYcW-g"
