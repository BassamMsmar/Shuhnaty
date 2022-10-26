from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



User = get_user_model()

class SingUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, required=False, help_text='Required! Inform a valid email address')
    number_phone = forms.CharField(max_length=16, required=False, help_text='966 5xxx xxxx xx')

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'number_phone',
       
        )