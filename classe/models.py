from django.db import models

class Classe(models.Model):
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)  # Ex: CP, CE1, 6ème, Terminale

    def __str__(self):
        return f"{self.niveau} - {self.nom}"
