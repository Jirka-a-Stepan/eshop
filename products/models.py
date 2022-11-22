from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User


class Producer(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(
        max_length=55,
        unique=True
    )

    def __str__(self):
        return self.name


class OperationSystem(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MobileStandard(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class SupportedEbookFormat(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class SimType(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


def product_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"images/products/product_{instance.pk}.{ext}"


class Product(models.Model):
    class ProductType(models.TextChoices):
        MOBILE = 'mobile', 'Mobile'
        TABLET = 'tablet', 'Tablet'
        EBOOK_READER = 'ebook_reader', 'E-Book Reader'

    name = models.CharField(max_length=200)
    product_type = models.CharField(
        max_length=15,
        choices=ProductType.choices,
        default=None
    )

    # if is_published is True alias is not possible to change
    is_published = models.BooleanField(default=False)

    producer = models.ForeignKey(Producer, on_delete=models.RESTRICT)
    alias = models.CharField(
        max_length=210,
        unique=True
    )

    description = models.TextField()
    images = models.ImageField(
        upload_to=product_path,
        null=True,
        blank=True
    )
    stock = models.PositiveIntegerField(default=0)
    prize = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)
    width = models.PositiveIntegerField(default=0)
    depth = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    insert_date = models.DateField(auto_now_add=True)
    display_size = models.DecimalField(
        default=0,
        max_digits=3,
        decimal_places=1
    )
    internal_memory = models.PositiveIntegerField(default=0)
    battery_capacity = models.PositiveIntegerField(default=0)
    operation_system = models.ForeignKey(
        OperationSystem,
        on_delete=models.RESTRICT,
        null=True,
        blank=True
    )
    mobile_standards = models.ManyToManyField(MobileStandard)
    sim_type = models.ManyToManyField(SimType)
    sim_number = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        blank=True
    )
    touched_display = models.BooleanField(
        default=True
    )
    supported_ebook_formats = models.ManyToManyField(
        SupportedEbookFormat,
        related_name='supported_ebook_formats',
        blank=True
    )
