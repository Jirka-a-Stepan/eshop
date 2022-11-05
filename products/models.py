from django.db import models
from django.contrib.auth.models import User


class Tablet(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Mobile(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
