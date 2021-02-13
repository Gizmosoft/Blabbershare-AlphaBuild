from django.db import models
from django.utils import timezone
# Create your models here.
class blogPost(models.Model):
    posttitle = models.CharField(max_length = 30)
    postdesc = models.TextField()

    date_added = models.DateTimeField(default = timezone.now)


def __str__(self):
    return 'Name:{}, ID:{}'.format(self.posttitle, self.id)
