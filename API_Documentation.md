#2-9-2024
# I tried registring user successfully
# I tried generating user tokenn by providing registered username password successfully.
# I tried to update authenticated user's profile successfully
# I tried to verify user's phone_number via otp using twilio package successfully.

# API Documentation

## EMployee Registration API

**Endpoint:** `POST http://127.0.0.1:8000/api/register/`
**Endpoint:** `POST /api/register/`

**Request Body:**

```json
{
  "username": "bunny0909g",
  "password": "password123",
  "email": "bunny@gmail.com",
  "phone_number": "9881167671",
  "date_of_birth": "2024-09-02"
}
**ResponseBody:**

```json
{
    "message": "Employee created successfully",
    "registration": {
        "id": 1,
        "username": "bunny0909g",
        "email": "bunny@gmail.com",
        "phone_number": "9881167671",
        "date_of_birth": "2024-09-02"
    }
}
Get Api token: http://127.0.0.1:8000/api/token/
      {
          "username": "bunny0909",
          "password": "password123"
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
REQUEST: PUT http://127.0.0.1:8000/profile/


BODY:
    {
        "city": "Pune"
    }
RESPONSE:
        {
            "id": 1,
            "employee": {
                "id": 1,
                "username": "bunny09",
                "email": "bunny2@gmail.com",
                "phone_number": "+919881167672",
                "date_of_birth": "2024-09-02"
            },
            "city": "Pune",
            "job_title": null,
            "company": null,
            "state": null,
            "profile_picture": "/media/profile_pictures/DE_tools.JPG"
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