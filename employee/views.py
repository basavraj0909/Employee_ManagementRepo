"""
***Access the API***
List Employees:    GET http://127.0.0.1:8000/api/employees/
Create Employee:   POST http://127.0.0.1:8000/api/employees/
Retrieve Employee: GET http://127.0.0.1:8000/api/employees/{id}/
Update Employee:   PUT http://127.0.0.1:8000/api/employees/{id}/
Partial Update :   PATCH http://127.0.0.1:8000/api/employees/{id}/
Delete Employee:   DELETE http://127.0.0.1:8000/api/employees/{id}/
"""

from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
import logging
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer

logger = logging.getLogger('employee')

class RegisterUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]  # Ensure anyone can access this endpoint

def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "User created successfully", "user": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        """
        Handle the creation of a new Employee.
        Args:
            request: The request object containing the data to create a new employee.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        Returns:
            Response: A DRF Response object containing a success message and the created
                      employee's data, along with an HTTP 201 Created status.
        Raises:
            Exception: If an error occurs during employee creation, the exception is
                       logged and raised to be handled by DRF's default error handling.
        """
        logger.info(f"Creating a new employee with data: {request.data}")
        try:
            response = super().create(request, *args, **kwargs)
            employee_id = response.data.get('id')
            logger.info(f"Employee created with ID: {employee_id}")
            return Response({"message": "Employee created successfully",
                             "data": response.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating employee:{str(e)}")
            raise

    def update(self, request, *args, **kwargs):
        """
        Handle the updating of an existing Employee.

        Args:
            request: The request object containing the data to update the employee.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments, including 'pk' which refers to the ID
                     of the employee being updated.

        Returns:
            Response: A DRF Response object containing a success message and the updated
                        employee's data, along with an HTTP 200 OK status.

        Raises:
            Exception: If an error occurs during the update process, the exception is logged
                       and raised to be handled by DRF's default error handling.
        """
        emp_id = kwargs.get('pk')
        logger.info(f"Updating employee with ID: {emp_id}")

        try:
            response = super().update(request, *args, **kwargs)
            logger.info(f"Updated employee with ID: {emp_id}")
            return Response({"message": "Employee updated successfully.",
                             "data": response.data},
                            status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f'Error updating employee: {str(e)}')
            raise

    def destroy(self, request, *args, **kwargs):
        """
        Handle the deletion of an existing Employee.

        Args:

            request: The request object initiating the deletion.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments, including 'pk' which refers to the ID
                     of the employee being deleted.

        Returns:
            Response: A DRF Response object containing a success message and an HTTP 204 No
                      Content status if the deletion is successful. In case of an error,
                      it returns an HTTP 400 Bad Request response with an error message.
        Raises:
            Http404: If the employee with the specified ID does not exist.
        """
        emp_id = kwargs.get('pk')
        logger.info(f"Attempting to delete employee with ID: {emp_id}")

        # Check if the employee exists
        employee = get_object_or_404(Employee, pk=emp_id)
        try:
            response = super().destroy(request, *args, **kwargs)
            logger.info(f"Employee deleted with ID: {emp_id}")
            return Response({"message": "Employee deleted successfully."},
                            status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            logger.error(f"Error deleting employee with ID {emp_id}: {str(e)}")
            return Response({"error": "An error occurred while deleting the employee."},
                            status=status.HTTP_400_BAD_REQUEST)
