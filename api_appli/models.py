from django.db import models


# Create your models here.
class Genre(models.Model):
    type = models.CharField(max_length=100)
    codeGenre = models.CharField(max_length=50)

    def __str__(self):
        return f"Genre {self.type}"


class Livre(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    status_lecture = models.BooleanField(default=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    note = models.IntegerField()


class Lecteur(models.Model):
    nom = models.CharField(max_length=20)
    prenoms = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    adresse = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField()


class Bibliothecaire(models.Model):
    nom = models.CharField(max_length=20)
    prenoms = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    adresse = models.CharField(max_length=15, null=True, blank=True)
    identifiant = models.CharField(max_length=10)
