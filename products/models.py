from django.db import models
from django.contrib.auth.models import User

class BaseProduct(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)

    class Meta:
        abstract = True

class Tablet(BaseProduct):

    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Mobile(BaseProduct):

    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
