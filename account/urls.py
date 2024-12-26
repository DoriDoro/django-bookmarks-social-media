from django.contrib.auth import views as auth_views
from django.urls import path

from account import views

app_name = "account"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # path("login/", views.user_login, name="login"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
