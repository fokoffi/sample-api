
# 1 -- INTRODUCTION

The purpose of this project is to create an API Challenge Prompt implementation. This readme.txt file explains how to use the simple application.


# 2 -- REQUIREMENTS

Below is a list of requirements to install the project and to allow the code to run successfully.

## 2.1 -- System Configuration

The code was written with python 2.7 in mind. So it is required that the machine that runs this code has python 2.7 installed.

Going forward, whenever python is mentioned as the program to be invoked from the command line prompt, the assumption is that it will be python2.7.

## 2.2 -- Python Packages


i) tornado -- Tornado is used web interface for the RESTFUL API.
    $ sudo pip install tornado

## 2.3 -- Operating system


The instructions assume that the commands being typed will be on linux machine.


# 3 -- SECURITY


## 3.1 HTTPS

The code currently runs on port 2016. For a production application, I would change the port number to 443. I would create a cert file and a key file. And I would use the following configuration to start the server:

```python
server = tornado.httpserver.HTTPServer(app, ssl_options={
    'certfile': '/path/to/server.cert',
    'keyfile': '/path/to/server.key'
})
```

The only caveat is that the application would have to run with some form of  elevated privileges because it's required to bind to port numbers below 1024.

## 3.2 Logging

As it stands, there's no implementation for logging. Python provides packages that are easy to import and connect to running code to solve this problem. Logging could be used to track behavior to track when the server experiences an unplanned outtage, or to keep track of false results.

## 3.3 Denial of Service

For a future release, if this code is to be publicly released, then additional code should be written to prevent a denial of service attack. A possible implementation could be to limit the number of requests served per second by a specific IP address.


# 4 -- USAGE

## 4.1 -- Installing as a service

The following commands assume that the contents of the application folder from the zip file are installed in the path location `/usr/local/tools/builds/`.

From the command line, run the following commands:

```
# cp /usr/local/tools/builds/bash/valep /etc/init.d/.
# cd /etc/init.d/
# update-rc.d valep defaults
```

From that point:

To start the service:
```
# service valep start
```

To stop the service:
```
# service valep stop
```

## 4.2 -- Running the python code


From a terminal window:

Starting the API server from the top level folder of attachment:

```
$ python valapi/endpoint.py
```

To test that the endpoint is up and running:

```
$ curl -H "Content-Type: application/json" -H "Accept: application/json" -X GET http://localhost:2016/
```

If you obtain a "welcome to the API" message, then everything is up and running.

To receive a sample valid result from the endpoint:

```
$ curl -H "Content-Type: application/json" -H "Accept: application/json" -X GET http://localhost:2016/valid/
{"status": "valid", "data": {"phone_number": "(310) 456-1234", "first_name": "John", "last_name": "Smith", "dob": "01/12/1972", "account_number": 42942315, "address": "333 W 35th St, Chicago, IL", "zip_code": "60616"}}
```

To receive a sample failed result from the endpoint:

```
$ curl -H "Content-Type: application/json" -H "Accept: application/json" -X GET http://localhost:2016/failed/
{"status": "failed", "fields": {"first_name": "missing required field"}, "data": {"phone_number": "(310) 654-3412", "first_name": "", "last_name": "McIntyre", "dob": "11/22/1982", "account_number": 42942315, "address": "One E161st St,Bronx,NY", "zip_code": "10451"}}
```


Sending JSON objects to the API server using curl (all valid):

```
$ curl -H "Content-Type: application/json" -H "Accept: application/json" -X POST -d '{"first_name": "Mary","last_name": "McIntyre","dob": "11/22/1982","address": "One E161st St,Bronx,NY", "zip_code": "10451", "phone_number": "3106543412", "account_number": 42942315 }' http://localhost:2016/api/
```

Sending JSON to the API server using curl (all failures):

```
$ curl -H "Content-Type: application/json" -H "Accept: application/json" -X POST -d '{"last_name": "","dob": "11/22/1582","address": "One E161st St,Bronx,NY", "zip_code": "104514", "phone_number": "31065434124", "account_number": 32942311 }' http://localhost:2016/api/
```


# 5 -- UNIT TESTING

To invoke the all unit tests, change directories to the project root folder that contains the README.md file. Then, run the following command:

```
$ python -m unittest discover
```

For a verbose output use the '-v' flag:

```
$ python -m unittest discover -v
```


# 6 -- ASSUMPTIONS

The following is a list of assumptions made writing the API.

## 6.1 -- API Response Format:

When all validation rules are satisfied, the following should be the response:

```json
{
    "status": "valid"
}
```

However, if any validation rule fails, the following should be the output:

```json
{
    "status": "failed", 
    "fields": {
        "first_name": "missing required field"
    }
}
```

Where the fields object should contain all fields that fail validation with an appropriate validation failure message.

Lastly, the full response including the fixed input should be as follows:

```json
{
    "status": "failed",
    "fields": {
        "first_name": "missing required field"
    }
    "data": {
        "first_name": "",
        "last_name": "McIntyre",
        "dob": "11/22/1982",
        "address": "One E161st St,Bronx,NY",
        "zip_code": "10451",
        "phone_number": "(310) 654-3412",
        "account_number": 42942315
    }
}
```

Where the fields section wouldn't be a part of the response if there were no failures.

## 6.2 -- No Address rules:

There are no address rules for the address field. This means for all addresses provided, they will be blindly accepted and assumed to be correct. This is the reason why there are no rules for it in the Validator pacakge, and no unit tests for it in the ValidatorUnitTests class.

## 6.3 -- Date of Birth (DOB) Format:

The code assumes the following formats are acceptable for data of birth:

* M/D/YY
* M/D/YYYY
* M/DD/YY
* M/DD/YYYY
* MM/D/YY
* MM/D/YYYY
* MM/DD/YY
* MM/DD/YYYY
* M-D-YY
* M-D-YYYY
* M-DD-YY
* M-DD-YYYY
* MM-D-YY
* MM-D-YYYY
* MM-DD-YY
* MM-DD-YYYY
* M.D.YY
* M.D.YYYY
* M.DD.YY
* M.DD.YYYY
* MM.D.YY
* MM.D.YYYY
* MM.DD.YY
* MM.DD.YYYY

Where:
* D and DD are integers indicating the day of the month.
* M and MM are integers indicating the month of the year.
* YY and YYYY are integers indicating the year.
* When the year is in YY format, the century 19, i.e., 19YY.

For future releases, additional code should be written that try to capture dates of birth spelled out such as 'Jan 10th 1974' for instance. To prevent scope creep of this release, this feature will be tabled.

When returning the date to the end user, the format of choice will be as follows:

`MM/DD/YYYY`

## 6.4 -- Phone Number Formats:

The code assumes that phone numbers will only be in the most commonly seen formats. They are as follows:

* DDDDDDDDDD
* D-DDD-DDD-DDDD
* D DDD DDD DDDD
* D (DDD) DDD-DDDD
* D (DDD) DDD - DDDD
* D.DDD.DDD.DDDD
* D-DDD-DDD-DDDD
* D. DDD . DDD . DDDD
* D - DDD - DDD - DDDD
* etc...

Essentially, the code accepts any possible permutation of 10 or 11 digits and '(', ')', '-', '.' and ' ' as valid.

When returning the data back to the end user, the format of choice will be as follows:

`(DDD) DDD-DDDD`

## 6.5 -- First Name and Last Name:

The code assumes any text combination is a valid name. When returning the name back to the end user, the format of choice is similar to a title, properly capitalized, unless the name is already formated like 'McIntyre', in which case the already formated name will be returned.

## 6.6 -- Zip Code Formats:

The code assumes the following zip code formats are correct:

* ZZZZZ-ZZZZ
* ZZZZZ - ZZZZ
* ZZZZZ ZZZZ
* ZZZZZZZZZ
* ZZZZZ

Where Z is is any digit. For simplicity of the project, we'll assume any punctiation outsize if a '-' is considered invalid.

When returning the data back to the end user, the two acceptable zip code formats are as follows:

* ZZZZZ-ZZZZ
* ZZZZZ

