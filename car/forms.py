from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['image', 'owner_name', 'whatsapp', 'car_name', 'brand', 'km', 'price', 'license_plate', 'location', 'status']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'car_name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'km': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'image': 'Imagem',
            'owner_name': 'Nome do Proprietário',
            'whatsapp': 'WhatsApp',
            'car_name': 'Nome do Carro',
            'brand': 'Marca',
            'km': 'Quilometragem',
            'price': 'Preço',
            'license_plate': 'Placa',
            'location': 'Localização',
            'status': 'Status',
        }


class CarFormWithoutStatus(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['image', 'owner_name', 'whatsapp', 'car_name', 'brand', 'km', 'price', 'license_plate', 'location']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'car_name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'km': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'image': 'Imagem',
            'owner_name': 'Nome do Proprietário',
            'whatsapp': 'WhatsApp',
            'car_name': 'Nome do Carro',
            'brand': 'Marca',
            'km': 'Quilometragem',
            'price': 'Preço',
            'license_plate': 'Placa',
            'location': 'Localização',
        }