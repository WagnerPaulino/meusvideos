from django.db import models
from django.db.models import Model

# Create your models here.
class Usuario(Model):
    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    dtNasciemento = models.DateField(null=True, blank=True)

class Video(Model):
    url= models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    resenha = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)