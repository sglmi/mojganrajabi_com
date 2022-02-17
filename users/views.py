from django.shortcuts import render, redirect

from .forms import SignupForm


def dashboard(reqeust):
    return render(reqeust, "users/dashboard.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = SignupForm()
    print(dir(form))
    return render(request, "users/signup.html", {"form": form})
