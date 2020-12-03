from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.nome