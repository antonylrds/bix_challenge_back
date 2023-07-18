from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from companies_api import urls as companies_urls
from users import urls as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(companies_urls)),
    path('users/', include(users_urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
