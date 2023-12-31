from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'new-password'}),
            'password1': forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
            'password2': forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        }

        model = get_user_model()
        fields = ('username', )
