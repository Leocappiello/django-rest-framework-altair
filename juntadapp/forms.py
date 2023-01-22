from django import forms

class CreateNewEvent(forms.Form):
    titleRoom = forms.CharField(label="Nombre de evento", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    passwordRoom = forms.CharField(label="Contraseña", max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    