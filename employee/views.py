from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


"""
***Access the API***
List Employees:    GET http://127.0.0.1:8000/api/employees/
Create Employee:   POST http://127.0.0.1:8000/api/employees/
Retrieve Employee: GET http://127.0.0.1:8000/api/employees/{id}/
Update Employee:   PUT http://127.0.0.1:8000/api/employees/{id}/
Partial Update :   PATCH http://127.0.0.1:8000/api/employees/{id}/
Delete Employee:   DELETE http://127.0.0.1:8000/api/employees/{id}/
"""