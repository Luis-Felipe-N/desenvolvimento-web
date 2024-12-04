# import django
from django.urls import  path
from users.views import *

app_name = "users"

urlpatterns = [
    path('register/', RegisterUsuarioView.as_view(), name="register"),
    path('register-vendedor/', RegisterVendedorView.as_view(), name="register-vendedor"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]