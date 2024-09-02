from django.urls import path
from . import views

urlpatterns = [
    path('otp/generate/', views.GenerateOTPView.as_view(), name='generate_otp'),
    path('otp/verify/',views.VerifyOTPView.as_view(), name='verify_otp'),
]
