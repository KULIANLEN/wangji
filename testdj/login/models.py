from django.db import models

# Create your models here.

class num(models.Model):
    dat = models.IntegerField()
    name = models.CharField(max_length=200,default='null')


