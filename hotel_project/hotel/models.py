from django.db import models
from django.utils import timezone

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return self.nom

class Chambre(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    type_chambre = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Chambre {self.numero} - {self.type_chambre}"

class ImageChambre(models.Model):
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='chambres/')

    def __str__(self):
        return f"Image pour {self.chambre}"

class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"{self.client.nom} - {self.chambre.numero}"

class Reservation(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    chambre = models.ForeignKey('Chambre', on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    date_reservation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client.nom} - {self.chambre.numero} du {self.date_debut} au {self.date_fin}"

# Service offert par l'hôtel
class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nom} - {self.prix} $"

# Service utilisé par un client dans une réservation
class ServiceReservation(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.reservation} - {self.service.nom} x {self.quantite}"
    
    def cout_total(self):
        return self.service.prix * self.quantite

