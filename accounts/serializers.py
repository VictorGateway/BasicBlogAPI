
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from accounts.models import CustomUser
from allauth.account.adapter import get_adapter
from dj_rest_auth.serializers import LoginSerializer

class CustomLoginSerializer(LoginSerializer):
    username=None

class CustomRegisterSerializer(RegisterSerializer):
    username=None
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')
    
    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'Last_name': self.validated_data.get('last_name', ''),
            
        }

    # override save method of RegisterSerializer
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save()
        adapter.save_user(request, user, self)
        return user