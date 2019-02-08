from django.db import models

# Create your models here.

class Richie(models.Model):
    name = models.CharField(max_length=40)
    locaction = models.CharField(max_length=60)

class Jobs(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    amount = models.IntegerField()
    creater = models.ForeignKey(Richie, on_delete=models.CASCADE)
