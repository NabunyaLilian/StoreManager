# StoreManager

Store Manager is a web application that helps store owners manage sales and product inventory  records. This application is meant for use in a single store. 

	
## Required Features 
- Store attendant can search and add products to buyer’s cart. 
- Store attendant can see his/her sale records but can’t modify them. 
- App should show available products, quantity and price. 
- Store owner can see sales and can ﬁlter by attendants. 
- Store owner can add, modify and delete products. 

## Frontend
- You can access frontend from here https://nabunyalilian.github.io/StoreManager/UI/login.html

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 


### Prerequisites for API

Things you need to install for the API to work

* Python 

### Installing

To deploy this application follow these steps;
* clone/download this project from git hub
```
 git clone https://github.com/NabunyaLilian/StoreManager.git

```
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

* This is the link to my postman collection https://documenter.getpostman.com/view/5384614/RWgxuawi



API Endpoints currently available are;


|__Http header__| __Endpoint__ | __Functionality__ | 
|------|-------------|------------|
|POST|  /api/v2/products       | create a product     |
|POST| /api/v2/sales           | create a sale order| 
|GET|  /api/v2/products        | Fetch all products   |
|GET|  /api/v2/sales           | Fetch all sale orders  |
|GET|  /api/v2/product/<int:product_id>     | Fetch a single product    |
|GET|  /api/v2/sale/<int:sale_id>   | Fetch a single sale order  |
|PUT|  /api/v2/product/<int:product_id>     | update a single product    |
|DELETE|  /api/v1/product/<int:product_id>     | delete a single product    |
|POST| /api/v2/auth/login           | login a user| 
|POST| /api/v2/auth/signup           | sign up a user| 
|GET| /api/v2/users           | get all users|
|PUT| /api/v2/admin/<int:user_id>           | give admin rights|  


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

* URL Versioning has been used to version this applications endpoint 

* Current versions available are:
* Version 1
* Version 2

## Deployment

* Version 1 is deployed on heroku, access it using this link https://lia-store-manager-app.herokuapp.com/
* Version 2 is deployed on heroku, also access it using this link https://lilianstoremanager-api.herokuapp.com/