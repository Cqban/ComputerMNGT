from django import forms 
from django.core.exceptions import ValidationError

class AddMachineForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom de la machine')
    mach = forms.CharField(required=True, label='Type de machine')
    maintenanceDate = forms.DateField(required=True, label='Date de mise à jour')

    def clean_date(self):
        data = self.cleaned_data["maintenanceDate"]
        #check si la date est antérieure ou non
        return data

    def clean_mach(self):
        data = self.cleaned_data["mach"]
        print("clean_mach",data)
        return data

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 6:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data

class AddPersonnelForm(forms.Form):
    num_secu = forms.CharField(required=True, label='Numéro de sécurité sociale du du Personnel')
    nom = forms.CharField(required=True, label='Nom du Personnel')
    prenom = forms.CharField(required=True, label='Prenom du Personnel')

    def clean_numsec(self):
        data = self.cleaned_data["num_secu"]
        return data

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        return data

    def clean_prenom(self):
        data = self.cleaned_data["prenom"]
        return data
