
# Profile Management App


This Django app manages user profiles. It automatically creates a user profile upon user registration and provides API endpoints for retrieving and updating profile information using Django REST Framework (DRF).

## Features

 - Automatic Profile Creation: A user profile is automatically created after user registration via Django signals.
 - Profile Fields: Users can manage their profile information, including:
    - City
    - Job Title
    - Company
    - State
    - (Optional) Profile Picture (commented out for now)
 - API Endpoints:
    - GET /profile/: Retrieves the authenticated user's     profile.
    - PUT /profile/: Updates the authenticated user's profile (partial update supported).
- Custom Authentication: Profile operations are restricted to authenticated users.


## Requirements

- Django: django==3.2.0
- Django REST Framework: djangorestframework==3.12.4
- Python: >=3.8
- Django App: The app is part of a larger project and depends on the employee app for the custom user model.
## Installation

1. Clone the repository:

    git clone https://github.com/your-username/profile-management.git




2. Navigate to the project directory and install dependencies:

pip install -r requirements.txt
3. Add the app to your Django project by including 'profile_management' in INSTALLED_APPS in your settings file.

4. Run migrations:

python manage.py migrate

## Models

The app includes a UserProfile model with a OneToOneField relationship to the custom user model (CustomUser from the employee app). The fields available in the profile include:

- city
- job_title
- company
- state

The UserProfile instance is automatically created when a user is registered, using Django signals (post_save).


## Serializers

The UserProfileSerializer is responsible for serializing the profile data. It uses CustomUserSerializer from the employee app to serialize the related user object.


## API Endpoints

Get User Profile

- Endpoint: /profile/
- Method: GET
- Description: Retrieve the authenticated user's profile.

Update User Profile
- Endpoint: /profile/
- Method: PUT
- Description: Update the authenticated user's profile. Partial updates are supported.
## Permissions

The UserProfileDetailView is protected using DRF's IsAuthenticated permission. Only authenticated users can access or modify their profile information.


## Usage

To test the API endpoints, you can use Postman or a similar API testing tool. Make sure to include an authentication token in the request headers.

