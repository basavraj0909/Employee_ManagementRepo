# API Documentation

## User Registration API

**Endpoint:** `POST /api/register/`

**Request Body:**

```json
{
    "username": "john_doe",
    "password": "password123",
    "first_name": "john",
    "last_name": "Doe",
    "email": "test1@example.com",
    "phone_number": "9881167671",
    "date_of_birth": "1990-01-01"
}


### Get userprofile 
REQUEST:
        GET http://127.0.0.1:8000/api/profile/

RESPONSE:
      {
          "user": {
              "id": 1,
              "username": "john_doe",
              "first_name": "john",
              "last_name": "Doe",
              "email": "test1@example.com",
              "phone_number": "9881167671"
          },
          "city": null,
          "job_title": null,
          "company": null,
          "state": null
      }

### update user profile by providing the valid access token
REQUEST:
        http://127.0.0.1:8000/api/profile/
BODY:
    {
        "city": "Pune"
    }
RESPONSE:
        {
            "user": {
                "id": 1,
                "username": "john_doe",
                "first_name": "john",
                "last_name": "Doe",
                "email": "test1@example.com",
                "phone_number": "9881167671"
            },
            "city": "Pune",
            "job_title": null,
            "company": null,
            "state": null
        }   

###=========================================================

### Blog POST API for authenticated users

REQUEST: GET http://127.0.0.1:8000/api/blogs/

RESPONSE:
      [
          {
              "id": 1,
              "title": "1st blog",
              "content": "1st blog"
          }
      ]


REQUEST: POST http://127.0.0.1:8000/api/blogs/

BODY:
      {
          "title": "1st blog",
          "content": "1st blog"
      }

RESPONSE:
      [
          {
              "id": 1,
              "title": "1st blog",
              "content": "1st blog"
          }
      ]

REQUEST: PUT http://127.0.0.1:8000/api/blogs/1/
      
BODY: 
      {
          "title": "updated1st blog",
          "content": "1st blog"
      }

RESPONSE:
        {
            "id": 1,
            "title": "updated1st blog",
            "content": "updated 1st blog"
        }