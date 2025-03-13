from django.db import models
from student.models import Eleve


class Paiement(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField(auto_now_add=True, )
    methode_paiement = models.CharField(max_length=50, choices=[
        ('Espèces', 'Espèces'),
        ('Mobile Money', 'Mobile Money'),
        ('Carte Bancaire', 'Carte Bancaire')
    ])

    def __str__(self):
        return f"Paiement {self.montant}€ - {self.eleve.nom} {self.eleve.prenom} {self.eleve.classe}"
    
    def save(self, *args, **kwargs):
        """Met à jour le solde de l'élève après le paiement"""
        super().save(*args, **kwargs)
        self.eleve.montant_total -= self.montant
        self.eleve.save()

