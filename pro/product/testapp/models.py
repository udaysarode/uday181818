from django.db import models

# Create your models here.
class Combinedata(models.Model):
    customer_id = models.IntegerField()
    pack1 = models.JSONField()
    pack2 = models.JSONField()