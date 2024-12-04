from django import forms
from django.core.exceptions import ValidationError

from users.models.Usuario import Usuario


class RegisterUsuarioForm(forms.ModelForm):

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        
        error_messages = {
            'required': 'Senha obrigatória',
            'invalid': 'Sua senha deve haver 8 ou mais caracteres',
            'noconfirm': 'As senhas não coincidem'
        }
    )

    confirmar_senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label="Confirmar Senha",
        error_messages = {
            'required': 'Senha obrigatória',
            'noconfirm': 'As senhas não coincidem'
        }
    )

    class Meta:
        model = Usuario
        fields = [
            'first_name', 
            'last_name',
            'username', 
            'email',
            'password'
        ]

    def clean(self):
        cleaned_data = super().clean()

        senha_primaria = cleaned_data.get("password")
        senha_secondaria = cleaned_data.get("confirmar_senha")

        if senha_primaria != senha_secondaria:

            self.add_error('password', 'As senhas não coincidem')

        if len(senha_primaria) < 8:
            self.add_error('password', 'Senha muito curta')

        return cleaned_data

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )