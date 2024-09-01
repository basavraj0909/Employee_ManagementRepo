from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from emp_routers_app.views import landing_page

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
    path('api/', include('employee.urls')),  # Include the employees app URLs
    path('api/', include('profile_management.urls')),  # Include the profile app URLs
    path('api/', include('blog.urls')),  # Include the blog app URLs

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('api/auth/', include('registration.urls')),
]
