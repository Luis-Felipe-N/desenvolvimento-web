from rest_framework import serializers
from users.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        # fields = '__all__'
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'is_vendedor', 
            'perfil_imagem'
        ]