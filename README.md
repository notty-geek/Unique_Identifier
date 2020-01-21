# Unique_Identifier

- Simple Unique Identifier Service Without Using UUID or any other third party Lib



## Purpose

It is a Simple Web Service which Generates Unique Identifier on Every Namespace Called.

# Requirements

* Python 3+
* Django
* Djangorestframework

# The services are:

* Create Unique Identifier

/newId/{namespace}

## Example

'''
https://localhost:8000/newId/abc
'''

## Folder structure

```
.
├── requirements.txt        # python requirements file
├── README.md               # this doc               	    
└── tasks             # Task folder where application is implemented
    └── views	        # Handlers which Talks with Buisness Logics
    └── services		  # Buisness Logic to Implement Unique ID's
    └── tests		      # Unit tests for Module
    └── urls		      # URL redirections Declaration
    └── models        # db Objects to be stored declared here if needed 
    
└── backend           # Main Production app
    └── settings	    # All Settings related to Microservices
    └── Urls		      # Url's Declared here
    └── wsgi		      # Primary Deployment platform for Django 
    └── asgi		      # Asynchronous Server Gateway for Services
    
 ```   
 
 ## Installation
    
```
pip install -r Requirenents.txt
```   
# Start Local Server

```
python manage.py runserver
```
