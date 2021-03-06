from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dtNasciemento = models.DateField(null=True, blank=True)


class Video(Model):
    id = models.AutoField(primary_key=True)
    url= models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False, related_name='videos')

class Resenha(Model):
    id = models.AutoField(primary_key=True)
    texto= models.CharField(max_length=1000)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='resenhas')