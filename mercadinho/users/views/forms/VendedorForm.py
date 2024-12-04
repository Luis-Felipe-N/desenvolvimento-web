from users.models.Vendedor import Vendedor
from django import forms

def validar_cpnj(cnpj):

    if len(cnpj)  < 14:
        raise forms.ValidationError(
            'CPNJ deve haver 14 caracteres',
            code="invalid"
        )
    elif cnpj.isnumeric() is not True:
        raise forms.ValidationError(
            'CPNJ deve haver somente números',
            code="invalid"
        )


class RegisterVendedorForm(forms.ModelForm):

    cnpj = forms.CharField(
        required=True,
        validators=[validar_cpnj],

    )

    class Meta:
        model = Vendedor
        fields = [
            'nome_loja',
            'cnpj',
            'endereco',
            'telefone'
        ]

    