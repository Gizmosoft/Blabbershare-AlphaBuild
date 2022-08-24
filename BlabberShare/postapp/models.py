from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from BlabberShare import settings


# Create your models here.

class Post(models.Model):
    # post_id     = models.AutoField(primary_key=True)
    post        = models.TextField(max_length=20000)
    image       = models.ImageField(upload_to='images', blank=True)
    hashtags    = models.TextField(blank=True)
    date_time   = models.DateTimeField(default=timezone.now)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)

