from django.db import models
from camelorder.models import camel_order
from common.common import gen_code
# Create your models here.

class user_data(models.Model):
    id = models.CharField(max_length=12 , primary_key=True)
    gacha_token = models.IntegerField(default=1)
    order_token = models.IntegerField(default=1)
    possessions = models.JSONField(default=list)
    user_inv_code = models.CharField(max_length=6, default="")
    invited = models.BooleanField(default=False)
    def query_methods(self):return{
        'id' : lambda : self.id,
        'gacha_token' : lambda : self.gacha_token,
        'order_token' : lambda : self.order_token,
        'possessions' : lambda : self.possessions,
        "orders" : lambda : list(camel_order.objects.filter(owner=self))
    }

