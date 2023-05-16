from django.db import models
from datetime import datetime

class Machine(models.Model):

    TYPES = (
        ('PC', ('PC - Utilise Windows 11')),
        ('Mac', ('Mac - Utilise MacOS')),
        ('Serveur', ('Serveur - Serveur pour déployer des VM')),
        ('Switch', ('Switch - Maintient et connect des serveurs')),
    )


    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=32)
    maintenanceDate = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    mach = models.CharField(max_length=32, choices=TYPES, default='PC')
    etat = models.BooleanField(default=False) 

    def __str__(self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

class Personnel(models.Model):

    SEXES = (
        ('Homme', ('Homme - Employé')),
        ('Femme', ('Femme - Employée')),
        ('Inconnu', ('Inconnu - ?')),
    )

    num_secu = models.CharField(primary_key=True,default=0,max_length=13)
    nom = models.CharField(max_length=8)
    prenom = models.CharField(max_length=8)
    sexe = models.CharField(max_length=7, choices=SEXES, default='Inconnu')

    def __str__(self):
        return str(self.num_secu) + " -> " + self.nom + " -> " + self.prenom

    def get_name(self):
        return str(self.num_secu) + " " + self.nom + " " + self.prenom