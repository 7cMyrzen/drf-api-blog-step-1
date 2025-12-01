from rest_framework import generics
from .models import Concessionnaire, Vehicule
from .serializers import ConcessionnaireSerializer, VehiculeSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class ConcessionnaireListCreateView(generics.ListCreateAPIView):
    queryset = Concessionnaire.objects.all()
    serializer_class = ConcessionnaireSerializer
    permission_classes = [AllowAny]

class ConcessionnaireDetailView(generics.RetrieveAPIView):
    queryset = Concessionnaire.objects.all()
    serializer_class = ConcessionnaireSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

class VehiculeListCreateView(generics.ListCreateAPIView):
    serializer_class = VehiculeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Vehicule.objects.filter(
            concessionnaire_id=self.kwargs['concessionnaire_id']
        )

    def perform_create(self, serializer):
        serializer.save(concessionnaire_id=self.kwargs['concessionnaire_id'])

class VehiculeDetailView(generics.RetrieveAPIView):
    serializer_class = VehiculeSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

    def get_queryset(self):
        return Vehicule.objects.filter(
            concessionnaire_id=self.kwargs['concessionnaire_id']
        )