from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View

# import timeago, datetime

# Create your views here.
def index(request):
    return render(request, "index.html")

def soon(request):
    return render(request, "soon.html")
