from django.utils import timezone

from django.db import models

# Create your models here.
class Actualite(models.Model):
    ActualiteId = models.AutoField(primary_key=True)
    ActualiteTitle = models.CharField(max_length=250)
    ActualiteDescription = models.CharField(max_length=500)
    ActualiteTag = models.CharField(max_length=250, blank=True)
    ActualiteDate = models.DateTimeField(default=timezone.now())
    ActualiteStatus = models.BooleanField(default=False,blank=True)
    ActualiteImage = models.ImageField(upload_to='media/actualite/',blank=True)


class Service(models.Model):
    ServiceId = models.AutoField(primary_key=True)
    ServiceTitle = models.CharField(max_length=250)
    ServiceDescription = models.CharField(max_length=500)
    actualite = models.ForeignKey(Actualite, on_delete=models.CASCADE,blank=True)
