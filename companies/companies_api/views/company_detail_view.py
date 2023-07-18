from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from companies_api.models import Company
from companies_api.serializers import CompanySerializer

class CompanyDetailApiView(APIView):
    def get_object(self, company_id):
        
        try:
            return Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return None
        
    def get(self, resquest, company_id, *args, **kwargs):
        company_instance = self.get_object(company_id)
        if not company_instance:
            return Response({'res': 'Company not found.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CompanySerializer(company_instance)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, company_id, *args, **kwargs):
        company_instance = self.get_object(company_id)
        
        data = {
            'name': request.data.get('name') if request.data.get('name') else company_instance.name
        }
        
        serializer = CompanySerializer(instance=company_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, company_id, *args, **kwargs):
        company_instance = self.get_object(company_id)
        if not company_instance:
            return Response({'res': 'Company not found.'}, status=status.HTTP_400_BAD_REQUEST)
        company_instance.delete()
        return Response({'res': 'Object removed.'}, status=status.HTTP_200_OK)