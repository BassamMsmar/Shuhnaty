from django import forms
from .models import AddDriverModel

class AddDriverForm(forms.ModelForm):
    class Meta:
        model = AddDriverModel
        fields = ("__all__")