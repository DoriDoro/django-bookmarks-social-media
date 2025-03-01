from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from account.models import Profile

UserModel = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Register form for new User instances"""

    class Meta:
        model = UserModel
        fields = ["username", "first_name", "email", "password1", "password2"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]
