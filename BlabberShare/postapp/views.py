from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Post
# import timeago, datetime

# Create your views here.
# def index(request):
#     return render(request, "index.html")
#
def soon(request):
    return render(request, "soon.html")

def dashboard(request):
    posts  = Post.objects.all().order_by('-date_time')
    return render(request, "dashboard.html",{'posts':posts})

# def blogpost(request, id):
#     post = Post.objects.filter(post_id=id)[0]
#     print(post)
#     return render(request, "dashboard.html")



'''
    then   = posts.date_time.datetime()
    # then   = Post.objects.get(Post.date_time)
    date   = datetime.datetime.now()
    ago    = timeago.format(datetime.datetime(then), date)
'''
