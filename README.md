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

```
https://localhost:8000/newId/abc
```

# Json Response

```

{
    "namespace": "abc2-20381240431579600071641"
}

```

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

## Trade-off

Time Latency Could be an Issue with the code Here. As It is very simple implementation and we can improve this by caching the created Unique Identifiers and using them for other namespaces.

There are many Thrid party Libraries which are very well-know for generating Uniquie Identifier

* UUID 

Python comes with UUID lib We could have simple Used UUID4() To generate the Unique ID. AS it generated 128-bit number and there are very small chances of collosion as it is 2^61 generated UUID with Unique 128  bits which has Very very small chances of collision 

The Main Traidoff with UUID is also Speed and latency. But is very good option for scalable distribited systems.


## Future Task

* Implement a caching system to speed up the  results and avoid collosions in long run by using same Generated Id's for different Namespaces.

* We can add Various Contsraints to make it more unique by adding the combinations of things like:

            time_low               
            time_mid                
            time_hi_version         
            clock_seq_hi_variant    
            clock_seq_low           
            node                   
            time                   
            clock_seq  
            hex
            int
            
            
 # DEPLOYED ON   
 
 ```
 http://sahilgeek1.pythonanywhere.com/newId/abc
```            
            
            

