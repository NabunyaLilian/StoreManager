[![Build Status](https://travis-ci.com/NabunyaLilian/StoreManager.svg?branch=get_all_sales_ft)](https://travis-ci.com/NabunyaLilian/StoreManager)  [![Coverage Status](https://coveralls.io/repos/github/NabunyaLilian/StoreManager/badge.svg?branch=get_all_sales_ft)](https://coveralls.io/github/NabunyaLilian/StoreManager?branch=get_all_sales_ft)  [![Maintainability](https://api.codeclimate.com/v1/badges/79a07349aa2d77166540/maintainability)](https://codeclimate.com/github/NabunyaLilian/StoreManager/maintainability)

# StoreManager

Store Manager is a web application that helps store owners manage sales and product inventory  records. This application is meant for use in a single store. 

	
## Required Features 
- Store attendant can search and add products to buyer’s cart. 
- Store attendant can see his/her sale records but can’t modify them. 
- App should show available products, quantity and price. 
- Store owner can see sales and can ﬁlter by attendants. 
- Store owner can add, modify and delete products. 




## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 


### Prerequisites for API

Things you need to install for the API to work

* Python 

### Installing

To deploy this application follow these steps;
* clone/download this project from git hub
* Extract the project and open it in an Editor forexample Vs code ,Pycharm or any editor of your choice.
* create a python virtual environment using the following command
```
 virtualenv  venv 

``` 
* In windows, navigate to scripts in the venv folder where the virtual environment exists.
```
 cd venv\scripts

```
*  Activate the virtual environment using the following command ;
```
activate

```
* In linux, activate the virtual environment using ;
```
source bin/activate

```
* Execute the application by running a a given command

```
 python run.py

``` 

* After running that command the server will start running at http://127.0.0.1:5000/ which is the default URI 

* use the endpoints given below to test the api using postman, which is the highly recommended app to use when testing api's.


API Endpoints currently available are;


|__Http header__| __Endpoint__ | __Functionality__ | 
|------|-------------|------------|
|POST|  /api/v1/products       | create a product     |
|POST| /api/v1/sales           | create a sale order| 
|GET|  /api/v1/products        | Fetch all products   |
|GET|  /api/v1/sales           | Fetch all sale orders  |
|GET|  /api/v1/product/<int:product_id>     | Fetch a single product    |
|GET|  /api/v1/sale/<int:sale_id>   | Fetch a single sale order  |




## Testing 

Tests can be run by running by installing pytest using the command below ;
```
 pip install pytest

```

Then after installing pytest, type the command below to run the tests
```
 pytest

```

You can also get the test coverage though this requires you to have installed pytest --cov by running the command below.
```
pip install pytest-cov
```
To get the test coverage, you type the command below.
```
 pytest --cov .
```

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - Python web framework used


## Versioning

URL Versioning has been used to version this applications endpoint 

Currently only version:1 is available 
