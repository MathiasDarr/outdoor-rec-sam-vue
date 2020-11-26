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
