from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Carro(models.Model):
    MARCA_CHOICES = [
        ('fiat', 'Fiat'),
        ('ford', 'Ford'),
        ('chevrolet', 'Chevrolet'),
        ('volkswagen', 'Volkswagen'),
        ('honda', 'Honda'),
        ('toyota', 'Toyota'),
        ('bmw', 'BMW'),
        ('mercedes', 'Mercedes'),
        ('audi', 'Audi'),
        ('outros', 'Outros'),
    ]
    
    COMBUSTIVEL_CHOICES = [
        ('gasolina', 'Gasolina'),
        ('etanol', 'Etanol'),
        ('flex', 'Flex'),
        ('diesel', 'Diesel'),
        ('eletrico', 'Elétrico'),
        ('hibrido', 'Híbrido'),
    ]
    
    marca = models.CharField(max_length=20, choices=MARCA_CHOICES)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quilometragem = models.IntegerField()
    combustivel = models.CharField(max_length=10, choices=COMBUSTIVEL_CHOICES)
    cor = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='carros/', blank=True, null=True)
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano}"
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

class Compra(models.Model):
    comprador = models.ForeignKey(User, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)
    preco_pago = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.comprador.username} - {self.carro}"
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
