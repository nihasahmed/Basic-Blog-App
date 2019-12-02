
from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$',
               'required':'', 'type': 'email'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'pattern': '^(?!.*[-_]{2,})(?=^[^-_].*[^-_]$)[\w-]{3,15}$', 'required':''}))
    password = forms.CharField(widget=forms.TextInput(
        attrs={'type':'password','class': 'form-control', 'pattern': '^(?=[^\d_].*?\d)\w(\w|[!@#$%]){7,20}', 'required':''}))
    cpassword = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'password', 'class': 'form-control', 'pattern': '^(?=[^\d_].*?\d)\w(\w|[!@#$%]){7,20}',
               'required': ''}))