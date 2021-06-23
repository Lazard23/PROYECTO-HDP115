from operator import attrgetter

from django.forms import *
from core.apps.models import *
from django import forms

class SubsidioAguaForm(ModelForm):
    class Meta:
        model = SubsidioAgua
        fields = '__all__'
        fields = ['pertenece', 'cantidad_consumo', 'recibo_agua']
        exclude = ['cantidad_subsidio']
        labels = {'pertenece': 'Beneficiario'}

        widgets = {
            'cantidad_consumo': NumberInput(
                attrs={
                    'class': 'form-control col-md-4',
                    'placeholder': 'cantidad consumida en metros cúbicos'
                }
            )}

    def save(self, commit=True):
        form = super()
        data = {}
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class SubsidioTransporteForm(ModelForm):
    class Meta:
        model = SubsidioTransporte
        fields = ['pertenece','frecuencia_uso','cantidad_buses','cantidad_microbuses']
        exclude = ['cantidad_subsidio']
        labels ={'pertenece':'Beneficiario'}
        widgets = {
            'cantidad_microbuses': NumberInput(
                attrs={
                    'class': 'form-control col-md-4',
                    'placeholder': 'cantidad de microbuses que toma en el periodo de tiempo seleccionado'
                }
            ),
            'pertenece': TextInput(attrs={
                'class':'form-control',
                'placeholder':'beneficiario del subsidio transporte',
                'autocomplete':'off'

            })

        }

    def save(self, commit=True):
        form = super()
        data = {}
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    #Hacer validaciones adicionales
    def clean(self):
        cleaned = super().clean()
        if cleaned['cantidad_buses'] < 0:
            self.add_error('cantidad_buses','La cantidad de buses debe ser una cantidad mayor a 0')
        if cleaned['cantidad_microbuses'] < 0:
            self.add_error('cantidad_microbuses','La cantidad de microbuses debe ser una cantidad mayor a 0')
        return cleaned



