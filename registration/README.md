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