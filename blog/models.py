
# Create your models here.
from django.db import models
from django.utils import timezone
from django.conf import settings

class Petbook(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    texto = models.TextField()
    criacao = models.DateTimeField(default=timezone.now)
    publicacao = models.DateTimeField(blank=True, null=True)
    quandoVacinou = models.DateTimeField(blank=True, null=True)
    vacina = models.CharField(max_length=250)
    ondeVacinou = models.CharField(max_length=250, blank=True, null=True)

def publish(self):
    self.publicacao = timezone.now()
    self.save()


def __str__(self):
    return self.titulo

