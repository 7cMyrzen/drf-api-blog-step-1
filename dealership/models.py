from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Concessionnaire(models.Model):
    nom = models.CharField(max_length=64)
    siret = models.CharField(
        max_length=14,
        validators=[MinLengthValidator(14), MaxLengthValidator(14)],
        unique=True
    )

    def __str__(self):
        return self.nom

class Vehicule(models.Model):
    TYPE_CHOICES = [
        ('auto', 'Voiture'),
        ('moto', 'Moto'),
    ]
    
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    marque = models.CharField(max_length=64)
    chevaux = models.PositiveIntegerField()
    prix_ht = models.DecimalField(max_digits=10, decimal_places=2)
    concessionnaire = models.ForeignKey(
        Concessionnaire, 
        on_delete=models.CASCADE,
        related_name='vehicules'
    )

    def __str__(self):
        return f"{self.get_type_display()} {self.marque} - {self.chevaux}ch"