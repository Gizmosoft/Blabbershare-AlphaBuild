from django.urls import path, include
from . import views

urlpatterns = [
    path('blog/', views.index, name='index'),
    path('ipform.html/', views.ipform, name='ipform'),


]
