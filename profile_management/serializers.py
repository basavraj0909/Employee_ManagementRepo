from rest_framework import serializers
from .models import UserProfile
from registration.serializers import EmployeeSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True) # Nest EmployeeSerializer
    # username = serializers.CharField(source='employee.username', read_only=True)
    # email = serializers.EmailField(source='employee.email', read_only=True)
    # phone_number = serializers.CharField(source='employee.phone_number', read_only=True)
    # date_of_birth = serializers.DateField(source='employee.date_of_birth', read_only=True)


    class Meta:
        model = UserProfile
        fields = '__all__'


    def update(self, instance, validated_data):
        # Handle updates to the nested Employee fields if they were writable
        employee_data = validated_data.pop('employee', {})
        employee = instance.employee

        for attr, value in employee_data.items():
            setattr(employee, attr, value)
        employee.save()

        # Handle updates to the UserProfile fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

