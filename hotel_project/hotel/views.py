from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import Client
from .forms import ChambreForm
from .models import Chambre, ImageChambre
from .models import Reservation
from .forms import ReservationForm
from django.db.models import Q
from django.contrib import messages
from .models import ServiceReservation
from django.contrib import messages
from .forms import ServiceReservationForm


def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm()
    return render(request, 'ajouter_client.html', {'form': form})

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'liste_clients.html', {'clients': clients})

def accueil(request):
    return render(request, 'accueil.html')

def ajouter_chambre(request):
    if request.method == 'POST':
        form = ChambreForm(request.POST)
        images = request.FILES.getlist('image')  # ← collecte des images
        if form.is_valid():
            chambre = form.save()
            for img in images:
                ImageChambre.objects.create(chambre=chambre, image=img)
            return redirect('liste_chambres')
    else:
        form = ChambreForm()
    return render(request, 'ajouter_chambre.html', {'form': form})

def liste_chambres(request):
    chambres = Chambre.objects.all()
    return render(request, 'liste_chambres.html', {'chambres': chambres})

def reserver_chambre(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_reservations')  # à créer plus tard
    else:
        form = ReservationForm()
    return render(request, 'reserver_chambre.html', {'form': form})

def liste_reservations(request):
    reservations = Reservation.objects.all()

    for reservation in reservations:
        services = ServiceReservation.objects.filter(reservation=reservation)
        total_services = sum([s.cout_total() for s in services])
        reservation.services = services
        reservation.total_services = total_services
        reservation.total_general = reservation.chambre.prix + total_services

    return render(request, 'liste_reservations.html', {'reservations': reservations})

def reserver_chambre(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            chambre = form.cleaned_data['chambre']
            date_debut = form.cleaned_data['date_debut']
            date_fin = form.cleaned_data['date_fin']

            # Vérifier les conflits
            conflits = Reservation.objects.filter(
                chambre=chambre,
                date_debut__lt=date_fin,
                date_fin__gt=date_debut
            )
            if conflits.exists():
                messages.error(request, "❌ Cette chambre est déjà réservée pour cette période.")
            else:
                form.save()
                messages.success(request, "✅ Réservation enregistrée avec succès.")
                return redirect('liste_reservations')
    else:
        form = ReservationForm()
    return render(request, 'reserver_chambre.html', {'form': form})

def ajouter_service_reservation(request):
    if request.method == 'POST':
        form = ServiceReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Service ajouté à la réservation.")
            return redirect('liste_reservations')  # Ou une autre page
    else:
        form = ServiceReservationForm()
    return render(request, 'ajouter_service_reservation.html', {'form': form})











