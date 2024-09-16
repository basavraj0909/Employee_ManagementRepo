
# OTP Verification App


This Django app provides OTP (One-Time Password) generation and verification for phone number authentication. It integrates with Twilio for sending OTPs and uses Django models to store and verify the OTPs. It also associates OTP verification with an `Employee` model from another app (`registration`).

## Features
- Generate and send OTP to a user's phone number using Twilio.
- Store OTPs in the database with expiration time.
- Verify OTP provided by the user.
- Mark the user's phone number as verified upon successful OTP verification.
- Customizable expiration time for OTPs.

## Prerequisites

1. **Django**: A Django project should already be set up.
2. **Twilio Account**: You'll need Twilio credentials to send OTP via SMS.
3. **Employee Model**: The app assumes that an `Employee` model with a `phone_number` and `is_phone_verified` field exists in the `registration` app.

## Installation

1. Clone or download the repository.
```bash
   git clone https://github.com/your-repo/otp-verification-app.git
   cd otp-verification-app
```

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

Generate OTP

- URL: /otp/generate/


- Method: POST

- Request Body:
    - {
        "phone_number": "1234567890"
        }

- Response
    - 200 OK: OTP sent successfully
    - 400 Bad Request: Phone number is required

Verify OTP

- URL: /otp/verify/

- Method: POST

- Request Body:
    - {
        "phone_number": "1234567890",
        "otp": "1234"}

- Response:

    - 200 OK: Phone number verified successfully
    - 400 Bad Request: OTP has expired or invalid
    - 404 Not Found: Employee not found



## Twilio Integration

Twilio is used to send OTPs to the user's phone number. Make sure you have an active Twilio account with the proper credentials and phone number in settings.py.

## Logging

The app logs OTP generation and sending using Django's built-in logging system. OTPs sent to the phone numbers are logged for debugging purposes.

## Running the App
    python manage.py runserver
Send a POST request to /otp/generate/ to generate and send an OTP. Use the /otp/verify/ endpoint to verify the OTP.

