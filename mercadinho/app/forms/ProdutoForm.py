from mercado.models.Produto import Produto
from django import forms

class ProdutoForm(forms.ModelForm):


    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'span-3'
            }
        )
    )

    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'span-3'
            }
        )
    )

    descricao_html = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'span-3'
            }
        ),
        required=False
    )

    com_desconto = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'label-row'
            }
        )
    )

    

    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'label-imagem',
                'data': 'inputImage'}
        )
    )
    
    class Meta:
        model = Produto
        fields = [
            'nome', 'descricao',
            'descricao_html', 'preco',
            'imagem', 'categoria',
            'desconto', 'com_desconto'
        ]

    def clean(self):

        cleaned_data = super().clean()

        com_desconto = cleaned_data.get('com_desconto')
        quant_desconto = cleaned_data.get('desconto')
        if com_desconto is True:

            if quant_desconto is None:
                self.add_error('desconto', 'Informe a quantidade de desconto')

            if quant_desconto < 0 or quant_desconto > 100:
                self.add_error('desconto', 'Insira um valor entre 0 à 100')


        return super().clean()