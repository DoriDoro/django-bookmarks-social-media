from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from account.forms import LoginForm


@login_required
def dashboard(request):
    return render(request, "dashboard.html", {"section": "dashboard"})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                request,
                username=cleaned_data["username"],
                password=cleaned_data["password"],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})
