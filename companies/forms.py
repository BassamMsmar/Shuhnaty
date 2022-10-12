from django import forms
from .models import AddCompanyModel


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = AddCompanyModel
        fields = ("__all__")