from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Employee Management API',
        default_version='v1',
        description="API documentation for the Employee Management application using url routers.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bningadali@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),  # Include the employees app URLs
    path('', include('otp_app.urls')),  # Include the employees app URLs
    path('', include('profile_management.urls')),  # Include the profile app URLs

    # path('api/', include('blog.urls')),  # Include the blog app URLs

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
