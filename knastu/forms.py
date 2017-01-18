from django import forms
from rest_service.models import *

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name',)

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('name', 'serial', 'contact', 'locations')