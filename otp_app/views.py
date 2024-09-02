from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from twilio.rest import Client
from .models import OTP
from .serializers import OTPVerificationSerializer
from registration.models import Employee
import random
import logging
from django.utils import timezone


logger = logging.getLogger(__name__)
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


class GenerateOTPView(generics.CreateAPIView):
    # This view generates and sends an OTP to the user's phone number

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        otp_value = random.randint(1000, 9999)
        from datetime import timedelta
        expires_at = timezone.now() + timedelta(minutes=5)  # Example expiration time

        # Save OTP in the database
        otp_record = OTP.objects.create(phone_number=phone_number, otp=otp_value, expires_at=expires_at)

        message = client.messages.create(
            body=f'Your verification code is {otp_value}',
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )

        logger.info(f'OTP sent to {phone_number}: {otp_value}')

        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)


class VerifyOTPView(generics.CreateAPIView):
    # This view verifies the OTP provided by the user
    serializer_class = OTPVerificationSerializer

    def post(self, request, *args, **kwargs):
        otp_value = request.data.get('otp')
        phone_number = request.data.get('phone_number')

        if not otp_value or not phone_number:
            return Response({'error': 'Phone number and OTP are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            otp_record = OTP.objects.get(phone_number=phone_number, otp=otp_value)
            if otp_record.is_expired():
                return Response({'error': 'OTP has expired, Please regenerate otp'}, status=status.HTTP_400_BAD_REQUEST)

            # Update registration status to verified
            employee = Employee.objects.get(phone_number=phone_number)
            print('-------------employee', employee)
            employee.is_phone_verified = True
            employee.save()

            # Optionally delete the OTP record after successful verification
            # otp_record.delete()
            return Response({'message': 'Phone number verified successfully'}, status=status.HTTP_200_OK)

        except OTP.DoesNotExist:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)





