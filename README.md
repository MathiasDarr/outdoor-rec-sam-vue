### Outdoor Recreation ECommerce Serverless Applications Model Vue Application ###

This repository contains applications developed using the  AWS serverless application model (SAM) as well as storefront front end.

### This repository contains ###
* Products & Orders Application
    * Products Database
        - Script for scraping product details & images from REI.com into DynamoDB table
        - Uses the following technologies
            - Selenium
            - BeautifulSoup 
            - Regex
    * Product Query API
        - Serverless Application for querying the products database
        - API defined via swagger
        - product detail route
        - query products by vendor (partition key) and query products by category using a global secondary index 
    * Orders API
        - Serverless API for viewing customers orders & posting orders
        - Lambda functions verify token sent in Authorization header
        - Lamba function & route for querying all customers orders
        - Lambda function & route for posting a new order 
    * Customers API
        - Serverless API for viewing customer information 
        - Lambda function triggers upon successful registration to Cognito User Pool, creating entry in Customers table
        - Customer detail route
        - Routes for updating customer information    

* Vue Front End
    * make requests to serverless API using axios
    * Authenticaition with a Cognito User Pool.  
        - returns JWT tokens 
    * Token is sent to lambda functions in Authorization header

<img src="https://dakobed-outdoor-recreation.s3-us-west-2.amazonaws.com/images/product_list.png" width="840" height="500">

### Running the web scraper and populating the database ###
* run the web scraper & populate the dynamo products table
    - cd data_model/rei_product_scraping
        - python3 scrape_rei_download_images.py
     - cd .. 
        - python3 populate_dynamo_products.py

### Running the frontend website ###
* cd outdoor-rec-storefront
    - npm install
    - npm run serve
