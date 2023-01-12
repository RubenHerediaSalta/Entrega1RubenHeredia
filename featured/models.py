from django.db import models

class Featured(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)