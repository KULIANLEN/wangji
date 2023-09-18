from django.db import models

# Create your models here.
class user_data(models.Model):
    id = models.CharField(max_length=12 , primary_key=True)
    gacha_token = models.IntegerField(default=1)
    order_token = models.IntegerField(default=1)
    possessions = models.JSONField(default=list)
