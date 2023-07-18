from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from companies_api.models import Employee
from companies_api.serializers import EmployeeSerializer

class EmployeeListView(APIView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'company': request.data.get('company_id')
        }
        
        serializer = EmployeeSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)