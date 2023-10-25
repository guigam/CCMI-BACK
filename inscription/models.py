from django.db import models



# Create your models here.
class Inscription(models.Model):
    InscriptionId = models.AutoField(primary_key=True)
    ParentInscription = models.ForeignKey(
        "Parent", on_delete=models.CASCADE)

    def __str__(self):
        return self.InscriptionId  # What you want to sho


class Parent(models.Model):
    ParentID = models.AutoField(primary_key=True)
    NomParent = models.CharField(max_length=250)
    PrenomParent = models.CharField(max_length=250)
    PhoneParent = models.CharField(max_length=100)
    EmailParent = models.CharField(max_length=250)

    def __str__(self):
        return self.NomParent + self.PrenomParent  # What you want to sho


class Enfant(models.Model):
    EnfantID = models.AutoField(primary_key=True)
    PrenomEnfant = models.CharField(max_length=250)
    DateNaissance = models.DateTimeField(blank=True)
    gender = models.BooleanField() #garcon = 1
    ParentEnfant = models.ForeignKey(
        "Parent", on_delete=models.CASCADE)
    def __str__(self):
        return  self.PrenomEnfant + self.ParentEnfant.NomParent