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
        description="API documentation for the Employee Management application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bningadali@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
    # authentication_classes=['rest_framework_simplejwt.authentication.JWTAuthentication',
    #                         ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employee.urls')),  # Include the employees app URLs


    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('', landing_page, name='landing-page'),  # Add this line for the landing page
    # path('api/', include('emp_routers_app.urls')),
]
