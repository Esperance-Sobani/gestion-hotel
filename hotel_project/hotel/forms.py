from django import forms
from .models import Client
from .models import Chambre, ImageChambre
from .models import Reservation
from .models import ServiceReservation

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'email', 'telephone']

class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['numero', 'type_chambre', 'prix', 'disponible']

class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['numero', 'type_chambre', 'prix', 'disponible']


from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['client', 'chambre', 'date_debut', 'date_fin']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }




class ServiceReservationForm(forms.ModelForm):
    class Meta:
        model = ServiceReservation
        fields = ['reservation', 'service', 'quantite']






