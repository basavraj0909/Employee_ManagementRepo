from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import logging
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def landing_page(request):
    """
    Renders the landing page displaying available links and resources.

    This view generates a landing page that provides users with
    direct links to various resources within the application, such
    as the Django Admin interface and Swagger API documentation.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of
                      available links/resources.
    """

    links = {
        "Django Admin": reverse("admin:index"),
        "Swagger API Documentation": reverse("schema-swagger-ui"),
        # "Employees API": reverse('employee-list'),
        # Add more links as needed
    }
    return render(request, "landing_page.html", {"links": links})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Employee registered"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeLoginView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            employee = Employee.objects.get(email=email)
            if check_password(password, employee.password):
                serializer = EmployeeSerializer(employee)
                logger.info(f"Employee {email} logged in successfully")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                logger.warning(f"Login attempt failed for {email}. Incorrect password.")
                return Response(
                    {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
                )
        except Employee.DoesNotExist:
            logger.warning(f"Login attempt failed. Employee {email} not found.")
            return Response(
                {"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND
            )
