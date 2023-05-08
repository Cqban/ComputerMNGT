from django.db import models
from datetime import datetime

class Machine(models.Model):

    TYPES = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy Virtual Machines')),
        ('Switch', ('Switch - Maintains and connect servers')),
    )


    id = models.AutoField(primary_key=True,editable=False)
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default=datetime.now())
    mach = models.CharField(max_length=32, choices=TYPES, default='PC') 

    def __str__(self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

class Personnel(models.Model):
    num_secu = models.CharField(primary_key=True,default=0,max_length=13)
    nom = models.CharField(max_length=8)
    prenom = models.CharField(max_length=8)

    def __str__(self):
        return str(self.num_secu) + " -> " + self.nom + " -> " + self.prenom

    def get_name(self):
        return str(self.num_secu) + " " + self.nom + " " + self.prenom