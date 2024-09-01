from rest_framework import serializers
from .models import Employee, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username','password',
                  'first_name', 'last_name','email', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    # user = CustomUser.objects.create_user(
    #         username=validated_data['username'],
    #         password=validated_data['password'],
    #         first_name=validated_data.get('first_name', ''),
    #         last_name=validated_data.get('last_name', ''),
    #         email=validated_data['email'],
    #         phone_number=validated_data['phone_number'],
    #         date_of_birth=validated_data.get('date_of_birth', None)
    #     )
    #     return user


class EmployeeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Employee
        # fields = ['user', 'position', 'date_joined', 'updated_at']
        fields = ['user', 'position']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUserSerializer().create(user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee