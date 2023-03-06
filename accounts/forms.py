from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        fields=("email",)


class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model= CustomUser
        fields = ("email", "first_name", "last_name")