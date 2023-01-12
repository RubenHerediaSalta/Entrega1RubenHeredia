from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()