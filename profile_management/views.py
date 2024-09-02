from rest_framework import generics,permissions
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status

class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(employee=self.request.user)
        return profile

    def put(self, request, *args, **kwargs):
        try:
            profile_record = UserProfile.objects.get(employee=request.user)
        except UserProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(profile_record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, *args, **kwargs):
#         try:
#             profile_record = UserProfile.objects.get(user=request.user)
#         except UserProfile.DoesNotExist:
#             return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = UserProfileSerializer(profile_record)
#         return Response(serializer.data)
#
#     def put(self, request, *args, **kwargs):
#         try:
#             profile_record = UserProfile.objects.get(user=request.user)
#         except UserProfile.DoesNotExist:
#             return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = UserProfileSerializer(profile_record, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
