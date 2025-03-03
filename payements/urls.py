from django.urls import path
from . import views

urlpatterns = [
    path('effectuer-paiement/', views.effectuer_paiement, name='effectuer_paiement'),
    path('liste-paiements/', views.liste_paiements, name='liste_paiements'),
]