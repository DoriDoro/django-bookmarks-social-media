from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from account.forms import UserRegistrationForm

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
    template_name = 'account/registration.html'
    success_message = "Your account was created successfully."
    success_url = reverse_lazy('account:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)

        return response
