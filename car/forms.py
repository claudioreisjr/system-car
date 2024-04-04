from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['image', 'owner_name', 'whatsapp', 'car_name', 'brand', 'km', 'price', 'license_plate', 'location', 'status']
