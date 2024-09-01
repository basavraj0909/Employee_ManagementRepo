from rest_framework import serializers
from .models import UserProfile
from employee.models import CustomUser
from employee.serializers import CustomUserSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = UserProfile
        # fields = ['user', 'city', 'job_title', 'company', 'state', 'profile_picture']
        fields = ['user', 'city', 'job_title', 'company', 'state']

