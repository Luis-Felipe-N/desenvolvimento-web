from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from users.models import Usuario

class RegisterUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password_confirm', 'is_vendedor', 'perfil_imagem']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})

        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})

        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')

        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario
