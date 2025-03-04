from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Model3D
from .models import Product




class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses bootstrap CSS."""
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'User name'
        })
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput({
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'price', 'lab_days']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product code'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'lab_days': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter lab days'}),
        }

class Model3DForm(forms.ModelForm):
    class Meta:
        model = Model3D
        fields = '__all__'
