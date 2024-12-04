from rest_framework import generics
from api.serializers import UsuarioSerializer
from users.models import Usuario
from django.db.models import Q

class UsuarioListAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(is_superuser=False, is_staff=False)
        # queryset = super().get_queryset()
        termo = self.request.query_params.get('query', None)

        if termo:
            queryset = queryset.filter(
                Q(first_name__icontains=termo) | Q(last_name__icontains=termo)
            )
            
        return queryset