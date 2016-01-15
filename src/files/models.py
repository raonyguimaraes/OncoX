from __future__ import unicode_literals
# from django.contrib.auth.models import User
from authtools.models import User

from django.db import models


# Create your models here.
class File(models.Model):
    
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    file = models.FileField()
    def __str__(self):
        return self.name