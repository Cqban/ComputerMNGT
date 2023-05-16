from django import forms 
from django.core.exceptions import ValidationError
from datetime import date

class AddMachineForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom de la machine')
    mach = forms.CharField(required=True, label='Type de machine')
    maintenanceDate = forms.DateField(required=True, label='Date de mise à jour')
    etat = forms.BooleanField(required=False, initial=False, label='Etat de la machine (On/Off)')

    def clean_date(self):
        data = self.cleaned_data["maintenanceDate"]
        if data < date.today:
             raise ValidationError(("La date ne peux pas être antérieure à aujourd'hui"))
        return data

    def clean_mach(self):
        data = self.cleaned_data["mach"]
        return data

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 16:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data

class AddPersonnelForm(forms.Form):
    num_secu = forms.CharField(required=True, label='Numéro de sécurité sociale du du Personnel')
    nom = forms.CharField(required=True, label='Nom du Personnel')
    prenom = forms.CharField(required=True, label='Prenom du Personnel')
    sexe = forms.CharField(required=True, label='Sexe du Personnel')

    def clean_numsec(self):
        data = self.cleaned_data["num_secu"]
        return data

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        return data

    def clean_prenom(self):
        data = self.cleaned_data["prenom"]
        return data
    
    def clean_sexe(self):
        data = self.cleaned_data["sexe"]
        return data
