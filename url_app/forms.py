# forms.py

from django import forms
from .models import SetUrlData

class SetURLDataForm(forms.ModelForm):
    class Meta:
        model = SetUrlData
        fields = '__all__'
