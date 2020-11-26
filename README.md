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
* Vue Front End



### Running the web scraper and populating the database ###
* run the web scraper & populate the dynamo products table
    - cd data_model/rei_product_scraping
        - python3 scrape_rei_download_images.py
        - python3 populate_dynamo_products.py
