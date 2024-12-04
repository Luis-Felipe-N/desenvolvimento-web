from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login

class LoginAPIView(APIView):
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

    def post(self, request, *args, **kwargs):
        """
        Autentica o usuário e cria uma sessão.
        """
        # Obtém os dados do corpo da requisição
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '').strip()

        # Verifica se o usuário já está autenticado
        if request.user.is_authenticated:
            return Response(
                {"detail": "Usuário já está logado. Faça logOut para entrar novamente."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Autentica o usuário
        user = authenticate(username=username, password=password)

        if user:
            # Realiza o login do usuário
            login(request, user)
            return Response(
                {"detail": "Login realizado com sucesso!"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Usuário ou senha inválidos."},
                status=status.HTTP_401_UNAUTHORIZED
            )