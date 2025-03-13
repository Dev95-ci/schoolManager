from django.db import models

class Classe(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    niveau = models.CharField(max_length=50, choices=[
        ('primaire', 'Primaire'),
        ('college', 'Collège'),
        ('lycee', 'Lycée'),
        
    ])
    annee_scolaire = models.CharField(max_length=9)  # ex: 2024-2025

    def __str__(self):
        return f"{self.nom} - {self.annee_scolaire}"
