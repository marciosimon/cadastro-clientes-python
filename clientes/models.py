from django.db import models

# Create your models here.
class Produto(models.Model):
    price = models.FloatField()
    image = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    id = models.UUIDField(primary_key=True)
    reviewScore = models.IntegerField()

    def __str__(self):
        return self.title


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, unique=True)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.nome


