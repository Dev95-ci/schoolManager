from django import forms
from .models import Eleve

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nom', 'prenom','telephone','matricule', 'date_naissance','montant_total', 'classe']
    
    def __init__(self, *args, **kwargs):
        super(EleveForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
