from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from twilio.rest import Client
from .models import OTP
from employee.models import Employee
import random
import datetime

import logging

logger = logging.getLogger(__name__)


class RegisterView(APIView):

    def post(self, request):
        """
        Handle the registration of an employee via phone number and OTP (One-Time Password).

        **POST Request:**
        - phone_number (str): The phone number of the employee.
        - first_name (str): The first name of the employee.
        - last_name (str): The last name of the employee.
        - email (str): The email address of the employee.

        **Response:**
        - 200 OK: OTP sent successfully.
        - 400 Bad Request: If any of the required fields are missing.
        - 409 Conflict: If the phone number is already verified.

        This view generates a one-time password (OTP) and sends it via SMS using Twilio.
        It also associates the OTP with the Employee model and stores the OTP in the OTP model.
        The OTP is valid for 10 minutes.
        """
        phone_number = request.data.get('phone_number')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')

        if not all([phone_number, first_name, last_name, email]):
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Save OTP associated with the Employee model
        employee, created = Employee.objects.get_or_create(
            phone_number=phone_number,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
            })

        if not created and employee.is_phone_verified:
            return Response({"error": "Phone number is already registered."},
                            status=status.HTTP_409_CONFLICT)

        # Generate OTP
        otp = str(random.randint(1000, 7777))
        expires_at = timezone.now() + datetime.timedelta(minutes=10)

        # Send OTP via SMS using Twilio
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f'''{otp} is your OTP for Registration request on FOODCOURT.
                \nValid for 10 mins.\nNever share OTP with anyone''',
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        # Save OTP
        OTP.objects.create(employee=employee, otp=otp, expires_at=expires_at)

        return Response({'message': 'OTP sent successfully'},
                        status=status.HTTP_200_OK)


class VerifyOtpView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')

        if not phone_number or not otp:
            return Response({"error": "Phone number and OTP are required"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            employee = Employee.objects.get(phone_number=phone_number)
            otp_record = OTP.objects.filter(employee=employee).last()
        except  Employee.DoesNotExist:
            return Response({'error': "Invalid phone number"},
                            status=status.HTTP_400_BAD_REQUEST)
        logger.debug(f"Received OTP: {otp}, Stored OTP: {otp_record.otp}")

        if otp_record.otp == otp and not otp_record.is_expired():
            # TODO Here, you can add logic to mark the employee as verified, if needed
            employee.is_phone_verified = True  # Assuming you have a field like this
            employee.save()

            # TODO Generate JWT token (optional)
            refresh = RefreshToken.for_user(employee)
            return Response({
                'refres': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)


# Req Body for registration
"""
{
    "phone_number": "+1234567890",
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "date_of_birth": "1990-01-01"
}
"""

"""
Register: POST /api/auth/register/
Verify OTP: POST /api/auth/verify-otp/
"""
