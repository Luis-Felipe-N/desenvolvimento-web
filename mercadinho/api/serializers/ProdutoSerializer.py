from rest_framework import serializers
from app.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        # fields = '__all__'
        fields = [
            'nome', 
            'descricao', 
            'descricao_html', 
            'is_descricao_html', 
            'is_ativo', 
            'preco', 
            'vendedor', 
            'imagem', 
            'categoria', 
            'desconto', 
            'com_desconto', 
            'data_criacao'
        ]