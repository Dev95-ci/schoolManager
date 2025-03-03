from django import forms
from .models import Paiement

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = ['eleve', 'montant', 'methode_paiement']
        widgets = {
            'eleve': forms.Select(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'methode_paiement': forms.Select(attrs={'class': 'form-control'}),
        }

