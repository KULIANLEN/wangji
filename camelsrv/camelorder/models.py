from django.db import models
# Create your models here.
class camel_order(models.Model):
    owner = models.ForeignKey('user.user_data', on_delete=models.DO_NOTHING)
    items = models.JSONField(default=dict)
    extra = models.JSONField(default=dict)
    complement = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, default=None)
    status = models.IntegerField(default=0)
class cp_inv_code(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    order = models.ForeignKey('camel_order', on_delete=models.CASCADE)