from datetime import datetime

from django.db import models



# Create your models here.
class Saison(models.Model):
    SaisonId = models.AutoField(primary_key=True)
    SaisonTitle = models.CharField(max_length=250,null=True)
    SaisonDescription = models.CharField(max_length=500,null=True)
    SaisonDateDebut = models.DateTimeField(null=True)
    SaisonDateFin = models.DateTimeField(null=True)
    SaisonDateMiseEnLigne = models.DateTimeField(null=True)

    def __str__(self):
        return self.InscriptionTitle


class Parent(models.Model):
    ParentID = models.AutoField(primary_key=True)
    NomParent = models.CharField(max_length=250)
    PrenomParent = models.CharField(max_length=250)
    PhoneParent = models.CharField(max_length=100)
    EmailParent = models.CharField(max_length=250)

    def __str__(self):
        return self.PrenomParent + self.NomParent


class Enfant(models.Model):
    EnfantID = models.AutoField(primary_key=True)
    PrenomEnfant = models.CharField(max_length=250)
    DateNaissance = models.DateTimeField(auto_now=True, null=True)
    gender = models.BooleanField() #garcon = 1
    ParentEnfant = models.ForeignKey(
        "Parent",on_delete=models.CASCADE())
    def __str__(self):
        return self.PrenomEnfant + self.ParentEnfant.NomParent

class Inscription(models.Model):
    InscriptionID = models.AutoField(primary_key=True)
    SaisonInscription = models.ForeignKey(
        "Saison", null=True, on_delete=models.CASCADE())
    InscriptionEnfant = models.ForeignKey(
        "Enfant", null=True,on_delete=models.CASCADE())
    def __str__(self):
        return (self.SaisonInscription.SaisonTitle +
                self.InscriptionEnfant.PrenomEnfant +
                self.InscriptionEnfant.ParentEnfant.NomParent)

