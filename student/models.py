from django.db import models
from classe.models import Classe

class Eleve(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=15, unique=True, null=None)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=15, blank=True, null=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, null=False,)
    montant_restant = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.classe}"