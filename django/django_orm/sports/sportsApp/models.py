from django.db import models

# Create your models here.


class Player(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    age = models.IntegerField()
    height = models.FloatField()
    fgPercentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
