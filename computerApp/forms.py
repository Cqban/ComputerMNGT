from django import forms 
from django.core.exceptions import ValidationError
from datetime import date
from .models import Personnel, Infrastructure

class AddInfraForm(forms.Form):
    nom = forms.CharField(required=True, label="Nom de l'infrastructure")
    responsable = forms.ModelChoiceField(required=True, queryset=Personnel.objects.all(), label='Responsable')


    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 32:
            raise forms.ValidationError("Erreur de format pour le champ nom")
        return data
    
    def clean_responsable(self):
        responsable = self.cleaned_data["responsable"]
        responsable_id = responsable.num_secu  # Obtenir la valeur de num_secu
        if not responsable_id:
            raise forms.ValidationError("Veuillez sélectionner un responsable valide")
        return responsable_id

class AddMachineForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom de la machine')
    mach = forms.CharField(required=True, label='Type de machine')
    maintenanceDate = forms.DateField(required=True, label='Date de mise à jour')
    etat = forms.BooleanField(required=False, initial=False, label='Etat de la machine (On/Off)')
    responsable = forms.ModelChoiceField(required=True, queryset=Personnel.objects.all(), label='Responsable')
    infra = forms.ModelChoiceField(required=True, queryset=Infrastructure.objects.all(), label='Infrastructure')

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
    
    def clean_responsable(self):
        responsable = self.cleaned_data["responsable"]
        responsable_id = responsable.num_secu  # Obtenir la valeur de num_secu
        if not responsable_id:
            raise forms.ValidationError("Veuillez sélectionner un responsable valide")
        return responsable_id
    
    def clean_infra(self):
        infra = self.cleaned_data["infra"]
        infra_id = infra.id  # Obtenir la valeur de infra.id
        if not infra_id:
            raise forms.ValidationError("Veuillez sélectionner une infrastructure valide")
        return infra_id

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
