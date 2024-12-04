from rest_framework.generics import CreateAPIView
from users.models import Usuario
from api.serializers import RegisterUsuarioSerializer

class UsuarioCreateAPIView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegisterUsuarioSerializer