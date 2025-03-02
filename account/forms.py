from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from account.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    """Register form for new User instances"""

    class Meta:
        model = UserModel
        fields = ["username", "first_name", "email", "password1", "password2"]

    def clean_email(self):
        """
        Django does not check for email uniqueness because the default User model does not enforce unique emails
        Ensure email is unique before saving.
        """
        data = self.cleaned_data["email"]
        if UserModel.objects.filter(email=data).exists():
            raise forms.ValidationError(
                "Email already exists. Please use a different one."
            )
        return data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email"]

    def clean_email(self):
        """Ensure email is unique before saving."""
        data = self.cleaned_data["email"]
        qs = UserModel.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError(
                "Email already in use. Please use a different one."
            )
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]
