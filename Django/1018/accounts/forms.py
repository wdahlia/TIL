from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']

        