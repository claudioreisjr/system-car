from django.db import models



class Car(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Disponível'),
        ('vendido', 'Vendido'),
    )

    #image = models.ImageField(upload_to='cars/', null=True, blank=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True, default='default_image.jpg')

    owner_name = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=20)
    car_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    km = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    license_plate = models.CharField(max_length=7)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='ativo')
     
    #vendido = models.BooleanField(default=False)  # Novo campo para indicar se o carro está vendido


#criando model para veiculos vendidos
class Vendidos(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f'{self.car.car_name} - {self.car.brand} - {self.status}'