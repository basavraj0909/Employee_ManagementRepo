from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics

from django.contrib.auth.hashers import check_password
from .models import Employee
from .serializers import EmployeeSerializer
import logging

logger = logging.getLogger(__name__)


class EmployeeRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Save the validated data to the database
            return Response({"message": "User registered"}, status=status.HTTP_201_CREATED)

        # If the data is not valid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeLoginView(APIView):

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        try:
            employee = Employee.objects.get(email=email)

            if check_password(password, employee.password):
                serializer = EmployeeSerializer(employee)
                logger.info(f'EMployee {email} logged in successfully')
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                logger.warning(f'Login attempt failed for {email}. Incorrect Password')
                return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        except Employee.DoesNotExist:
            logger.warning(f'login attempt failed. Employee {email} not found.')
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
