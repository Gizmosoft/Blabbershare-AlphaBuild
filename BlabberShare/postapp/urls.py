from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('soon/', views.soon,  name='soon'),
    path('dashboard/', views.soon,  name='dashboard'),  #need to change here later.
]
