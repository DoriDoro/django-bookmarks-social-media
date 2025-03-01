from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Default User model does not enforce unique emails!"""

    email = models.EmailField(unique=True)


class Profile(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
