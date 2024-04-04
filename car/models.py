from django.db import models

# Create your models here.
from django.db import models

class Car(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('vendido', 'Vendido'),
    )

    image = models.ImageField(upload_to='cars/', null=True, blank=True)

    owner_name = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=20)
    car_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    km = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    license_plate = models.CharField(max_length=7)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='ativo')
