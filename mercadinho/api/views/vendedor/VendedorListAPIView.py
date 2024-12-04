from rest_framework import generics
from users.models import Vendedor
from api.serializers import VendedorSerializer

class VendedorListAPIView(generics.ListAPIView):
    queryset = Vendedor.objects.all() 
    serializer_class = VendedorSerializer 
