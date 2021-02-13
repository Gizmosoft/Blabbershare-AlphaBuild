from django.urls import path, include
from . import views

urlpatterns = [
    path('blog/', views.blogIndex, name='blogIndex'),
    path('ipform.html/', views.ipform, name='ipform'),


]
