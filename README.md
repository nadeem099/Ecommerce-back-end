# Ecommerce-back-end
This is a repo for backend of an e-commerce application (A t-shirt selling website).

## Overview
This backend is built on python django rest api. 
This backend has following features(Apps):
1) Products: Lets you add, delete products.
2) Category: Handles categories of your product.
4) Order: Creates order.
3) Payment: Lets you create payments through baintree.
4) user: Manages your users.

## How to get started 
1) Fork this repo
2) Clone your forked repo
3) Create a new branch

## After creating a new branch follow below steps
1) This project is created on pipenv environment. You just have to go to your project directory and run ```pipenv shell```, It will install all the required dependencies needed to run the api. (note: to install pipenv use ```pip install pipenv```).
2) You need to create a super user in order to login to the admin app. To create a super user, go to the directory where ```manage.py``` is located and use command ```python manage.py createsuperuser```.
3) Now run ```python manage.py runserver``` in order to run the localhost server.
4) Go to ```localhost/admin``` or use the given url that you see after running the server with ```/admin``` in order to see the admin app.
5) Use your credentials of super user to login to admin app.

## The other useful api directories are
```http://127.0.0.1:8000/api/```

```http://127.0.0.1:8000/api/product/```

```http://127.0.0.1:8000/api/category/```

```http://127.0.0.1:8000/api/order/```

```http://127.0.0.1:8000/api/user/```

## Follow the below link for the front end built using this api
[E-commerce front end built using Reactjs](https://github.com/nadeem099/ECommerce-front-end)
