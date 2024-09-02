from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Employee

class EmployeeTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls,employee):
        token = super().get_token(employee)
        token['username'] = employee.username
        return token

    def validate(self, attrs):

        try:
            employee = Employee.objects.get(username=attrs['username'])
        except Employee.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password")

        if not employee.check_password(attrs['password']):
            raise serializers.ValidationError("Invalid username or password")

        refresh = self.get_token(employee)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'username', 'password', 'email', 'phone_number', 'date_of_birth']

    def create(self, validated_data):
        password = validated_data.pop('password')
        employee = Employee(**validated_data)
        employee.set_password(password)
        employee.save()

        return employee