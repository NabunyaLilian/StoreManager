[![Build Status](https://travis-ci.com/NabunyaLilian/StoreManager.svg?branch=get_all_sales_ft)](https://travis-ci.com/NabunyaLilian/StoreManager)

[![Coverage Status](https://coveralls.io/repos/github/NabunyaLilian/StoreManager/badge.svg?branch=get_all_sales_ft)](https://coveralls.io/github/NabunyaLilian/StoreManager?branch=get_all_sales_ft)

[![Maintainability](https://api.codeclimate.com/v1/badges/79a07349aa2d77166540/maintainability)](https://codeclimate.com/github/NabunyaLilian/StoreManager/maintainability)

# StoreManager

Store Manager is a web application that helps store owners manage sales and product inventory  records. This application is meant for use in a single store. 

	
## Features 
- 1. Store attendant can search and add products to buyer’s cart. 
- 2. Store attendant can see his/her sale records but can’t modify them. 
- 3. App should show available products, quantity and price. 
- 4. Store owner can see sales and can ﬁlter by attendants. 
- 5. Store owner can add, modify and delete products. 




## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 


### Prerequisites

What things you need to install the software

* Python 

### Installing

A step by step series of examples that tell you how to get a development env running

To deploy this application follow the following steps
* clone the project from git hub
* create a python virtual environment and install all the libraries in the "requirements.txt" file 
* navigate to the root of the project and execute the application by running a command "python run.py"

Once the application starts running. Then you can proceed to test the application using postman. The application by default runs on port 5000
. If everything is done perfect you will see a url like http://127.0.0.1:5000/ can be used to access the application through a browser.

These are the endpoints that are currently available


|__Type__| __Endpoint__ | __What the endpoint does__ | 
|------|-------------|------------|
|POST|  /api/v1/products       | used for adding a product    |
|POST| /api/v1/sales       | used to add a specific sales| 
|GET|  /api/v1/products      | returns all products and their details    |
|GET|  /api/v1/sales       | returns all sales made   |
|GET|  /api/v1/product/<int:product_id>     | returns a specific product     |
|GET|  /api/v1/sale/<int:sale_id>   | used to return a specific sale   |




## Running the tests

Tests can be run by running the command below at the root of the project directory
```
if not installed run "pip install pytest" to install pytest
then "pytest" to run the test
```


You can also get the test coverage by running the command below. this requires you to have installed pytest --cov

```
then type pytest --cov .
```

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - Python web framework used


## Versioning

URL Versioning has been used to version this applications endpoint 

Currently only version:1 is available 
