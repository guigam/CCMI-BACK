from django.utils import timezone

from django.db import models

# Create your models here.
class Actualite(models.Model):
    ActualiteId = models.AutoField(primary_key=True)
    ActualiteTitle = models.CharField(max_length=250)
    ActualiteDescription = models.CharField(max_length=500)
    ActualiteTag = models.CharField(max_length=250, blank=True)
    ActualiteDate = models.DateTimeField(blank=True)
    ActualiteImage = models.ImageField(upload_to='media/actualite/',blank=True)
    def __str__(self):
        return self.ActualiteTitle  # What you want to sho


