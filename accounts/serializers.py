
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from allauth.account  import app_settings as allauth_account_settings
from accounts.models import CustomUser
from allauth.account.adapter import get_adapter


class CustomRegisterSerializer(RegisterSerializer):
    username=None
    first_name = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2',)
    
    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            
        }

    # override save method of RegisterSerializer
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        
        user.save()
        adapter.save_user(request, user, self)
        return user