from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model

from .forms import LoginForm, RegisterForm

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.INFO, "User already logged in.") # Sending message to the user
        return redirect('/')

    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context['form'] = LoginForm()
            print("Error logging in.")

    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        messages.add_message(request, messages.INFO, "User Registered successfully!") # Sending message to the user
        return redirect('/')
    return render(request, "auth/register.html", context)

def logout_operation(request):
    logout(request)
    messages.add_message(request, messages.INFO, "User Logged out. Please login again to access content") # Sending message to the user
    return redirect('/')