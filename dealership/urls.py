from django.urls import path
from . import views

app_name = 'dealership'

urlpatterns = [
    path('concessionnaires/', views.ConcessionnaireListCreateView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:id>/', views.ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    path('concessionnaires/<int:concessionnaire_id>/vehicules/', views.VehiculeListCreateView.as_view(), name='vehicule-list'),
    path('concessionnaires/<int:concessionnaire_id>/vehicules/<int:id>/', views.VehiculeDetailView.as_view(), name='vehicule-detail'),
]