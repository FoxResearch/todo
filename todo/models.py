from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Usuario(models.Model):
    nombreusuario = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreusuario

@python_2_unicode_compatible  # only if you need to support Python 2
class Nota(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    titulo = models.TextField(max_length=200)
    texto = models.TextField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)
    publico = models.BooleanField(default=False)

    def es_reciente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.titulo
