from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from django.contrib.auth.hashers import check_password
from .models import Employee
from .serializers import EmployeeSerializer
import logging

logger = logging.getLogger(__name__)


class EmployeeRegisterView(APIView):
    """
   API endpoint for registering a new employee.

   This endpoint allows users to register by providing their details
   such as first name, last name, email, mobile number, and password.
   On successful registration, the user details are saved in the database,
   and a success message is returned.

   Request Body:
   - fname: First name of the employee (string)
   - lname: Last name of the employee (string)
   - mobile: Mobile number of the employee (string)
   - email: Email address of the employee (string)
   - password: Password for the account (string)

   Response:
   - 201: User registered successfully.
   - 400: Bad request if the data provided is not valid.
   """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Save the validated data to the database
            return Response({"message": "User registered"}, status=status.HTTP_201_CREATED)

        # If the data is not valid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeLoginView(APIView):
    """
    API endpoint for employee login.

    This endpoint allows employees to log in by providing their email and password.
    If the credentials are correct, the employee's details are returned. If not,
    an error message is returned.

    Request Body:
    - email: Email address of the employee (string)
    - password: Password for the account (string)

    Response:
    - 200: Employee logged in successfully, returns employee details.
    - 404: Employee not found or incorrect password.
    """

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        try:

            employee = Employee.objects.get(email=email)

            if check_password(password, employee.password):
                serializer = EmployeeSerializer(employee)
                logger.info(f'Employee: {email}, logged in successfully')
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                logger.warning(f'Login attempt failed for {email}. Incorrect Password')
                return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        except Employee.DoesNotExist:
            logger.warning(f'login attempt failed. Employee {email} not found.')
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
