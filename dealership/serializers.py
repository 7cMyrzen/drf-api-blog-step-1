from rest_framework import serializers
from .models import Concessionnaire, Vehicule

class ConcessionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = ['id', 'nom']
        read_only_fields = ['id']

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = ['id', 'type', 'marque', 'chevaux', 'prix_ht', 'concessionnaire']
        read_only_fields = ['id']