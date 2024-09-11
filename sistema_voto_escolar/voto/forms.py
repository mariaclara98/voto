# forms.py
from django import forms
from .models import Voto

class VotoForm(forms.ModelForm):
    class Meta:
        model = Voto
        fields = ['estudiante', 'lista']
