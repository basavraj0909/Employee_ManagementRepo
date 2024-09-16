## User Registration API
This API allows users to register by providing their username, password, and other required details.

### Endpoint
POST /api/register/

### Request Body
{
    "username": "bunny0909",
    "password": "password123",
    "first_name": "Basavraj",
    "last_name": "Ningadali",
    "email": "test@example.com",
    "phone_number": "9881167671",
    "date_of_birth": "1990-01-01"
}

### Obtaining token

### Endpoint
POST /api/token/

### Request Body
{"username": "bunny0909",
"password": "password123"}

### Response Body
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyOTc3NTc2LCJqdGkiOiJkNzVmMzM1Mi03MzU0LTQ3YzEtOTQ3YS00YzI4ZWI0YzU1NDdiIiwiaWQiOjF9.7vN40G-302tXli61Qj6_M1stNwc1vK1s7s1n71806K9_b9h999",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyOTc3NTc2LCJqdGkiOiJkNzVmMzM1Mi03MzU0LTQ3YzEtOTQ3YS00YzI4ZWI0YzU1NDdiIiwiaWQiOjF9.7vN40G-302tXli61Qj6_M1stNwc1vK1s7s1n71806K9_b9h999"
}




# need to update readme, will continue below

# Employee Management System


This is a Django-based Employee Management System that provides REST API endpoints for managing employees, generating and verifying OTPs, and authenticating users using JWT. The application leverages Django REST Framework (DRF) and Twilio for sending OTPs.

## Features
- **Employee Management**: Perform CRUD operations on employee data.
- **JWT Authentication**: Secure the API using JSON Web Tokens (JWT) with token generation and refresh endpoints.
- **OTP Verification**: Generate and verify OTPs for phone number verification.
- **Logging**: Record log messages for key actions like employee creation, updates, and deletion.

## Setup and Installation


## Prerequisites

1. Python 3.x
2. Django
3. Django REST Framework
4. Django SimpleJWT
5. Twilio API (for OTP)


3. Add the following configurations to your settings.py file:
- TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
- TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
- TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

4. Add the otp_app and registration apps to INSTALLED_APPS in settings.py.
    - INSTALLED_APPS = [
        'otp_app',
        'registration',
        ]

5. Run migrations to create the OTP model.

python manage.py migrate


## Models

OTP

The OTP model stores OTP codes for phone number verification. The OTP is associated with a phone number and has an expiration time.


Field	          Type	         Description

phone_number	CharField	     The phone number associated with  the OTP.

otp	            CharField	     The 4-digit OTP sent to the user.

created_at	    DateTimeField	 The date and time when the OTP was created.

expires_at	    DateTimeField	 The date and time when the OTP will expire.
# API Endpoints

**Employee Endpoints**

    List Employees:
        GET /api/employees/

    Create Employee:
        POST /api/employees/

    Retrieve Employee:
        GET /api/employees/{id}/

    Update Employee:
        PUT /api/employees/{id}/

    Partial Update:
        PATCH /api/employees/{id}/

    Delete Employee:
        DELETE /api/employees/{id}/

**Authentication Endpoints**
- Token (JWT) Obtain:
    - POST /api/token/
        - Request Body:
        {
        "username": "your_username",
        "password": "your_password"
        }

- Token Refresh:
    - POST /api/token/refresh/
        - Request Body:

            {
            "refresh": "your_refresh_token"
            }

