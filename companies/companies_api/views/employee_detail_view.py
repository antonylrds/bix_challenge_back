from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from companies_api.models import Employee
from companies_api.serializers import EmployeeSerializer

class EmployeeDetailView(APIView):
    def get_object(self, employee_id):    
        try:
            return Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return None

    def get(self, request, employee_id, *args, **kwargs):
        employee_instance = self.get_object(employee_id)
        if not employee_instance:
            return Response(
                {'res': 'Object with employee id does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = EmployeeSerializer(employee_instance)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, employee_id, *args, **kwargs):
        employee_instance = self.get_object(employee_id)
        if not employee_instance:
            return Response(
                {'res': 'Object with employee id does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        request_data = request.data
            
        data = {
            'name': request_data.get('name') if request_data.get('name') else employee_instance.name,
            'email': request_data.get('email') if request_data.get('email') else employee_instance.email,
            'company': request_data.get('company_id') if request_data.get('company_id') else employee_instance.company.id
        }
        
        print(employee_instance.company)
        
        serializer = EmployeeSerializer(instance=employee_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, employee_id, *args, **kwargs):
        employee_instance = self.get_object(employee_id)
        if not employee_instance:
            return Response({'res': 'Employee not found.'}, status=status.HTTP_400_BAD_REQUEST)
        employee_instance.delete()
        return Response({'res': 'Employee deleted'}, status=status.HTTP_200_OK)