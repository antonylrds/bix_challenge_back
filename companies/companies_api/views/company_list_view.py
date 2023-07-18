from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

from companies_api.models import Company
from companies_api.serializers import CompanySerializer

class CompanyListApiView(APIView):
    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @permission_classes((IsAdminUser,))
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name')
        }
        
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)