from django.urls import path, include

from account import views

app_name = "account"

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("registration/", views.UserRegisterView.as_view(), name="registration"),
    path("edit/", views.UserProfileEditView.as_view(), name="edit"),
]
