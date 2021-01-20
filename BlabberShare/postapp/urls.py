from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('soon/', views.soon,  name='soon'),
    path('dashboard/', views.dashboard,  name='dashboard'),
]
