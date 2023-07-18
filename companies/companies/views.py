from django.contrib.auth.models import update_last_login

from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request):
        result = super(CustomTokenObtainPairView, self).post(request)
        try:
            request_user, data = requests.get_parameters(request)
            user = requests.get_user_by_username(data['username'])
            update_last_login(None, user)            
        except Exception as exc:
            return None
        return result