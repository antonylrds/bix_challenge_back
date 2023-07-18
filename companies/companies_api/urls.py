from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    CompanyListApiView,
    CompanyDetailApiView,
    EmployeeListView,
    EmployeeDetailView
)

urlpatterns = [
    path('companies', CompanyListApiView.as_view()),
    path('companies/<str:company_id>', CompanyDetailApiView.as_view()),
    path('employees', EmployeeListView.as_view()),
    path('employees/<str:employee_id>', EmployeeDetailView.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]