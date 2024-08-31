# Registration App

## Purpose
The Registration app handles user sign-up, including OTP verification via mobile.

## Installation & Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Add `'registration'` to your `INSTALLED_APPS` in `settings.py`.
3. Run migrations: `python manage.py migrate registration`.

## Usage
- API Endpoints:
  - `POST /register/` - Register a new user.
  - `POST /verify-otp/` - Verify OTP for a registered user.

## Configuration
- Set `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` in your environment variables.

## Testing
- Run `python manage.py test registration` to execute tests.

## Known Issues
- None currently.
