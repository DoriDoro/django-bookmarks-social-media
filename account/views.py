from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from account.forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from account.models import Profile

UserModel = get_user_model()


class DashboardView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = "account/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = "dashboard"

        return context


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = UserModel
    form_class = UserRegistrationForm
    template_name = "account/registration.html"
    success_message = "Your account was created successfully."
    success_url = reverse_lazy("account:dashboard")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        Profile.objects.create(user=self.object)

        return response


class UserProfileEditView(LoginRequiredMixin, View):
    """
    Handle UserEditForm and ProfileEditForm to update both User and Profile instance.
    - SuccessMessageMixin impossible to use in View
    """

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        return render(
            request,
            "account/edit.html",
            {"user_form": user_form, "profile_form": profile_form},
        )

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("account:dashboard")
        else:
            messages.error(request, "Error updating your profile!")

        return render(
            request,
            "account/edit.html",
            {"user_form": user_form, "profile_form": profile_form},
        )
