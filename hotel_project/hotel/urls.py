from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('ajouter-client/', views.ajouter_client, name='ajouter_client'),
    path('clients/', views.liste_clients, name='liste_clients'),

    path('ajouter-chambre/', views.ajouter_chambre, name='ajouter_chambre'),
    path('chambres/', views.liste_chambres, name='liste_chambres'),
    path('reserver/', views.reserver_chambre, name='reserver_chambre'),
    path('reservations/', views.liste_reservations, name='liste_reservations'),
    path('ajouter-service/', views.ajouter_service_reservation, name='ajouter_service_reservation'),
    path('rapport-reservations/', views.rapport_reservations, name='rapport_reservations'),
    path('rapport-reservations/', views.rapport_reservations, name='rapport_reservations'),
    


]
