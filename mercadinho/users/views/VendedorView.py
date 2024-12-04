from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView
from users.forms.VendedorForm import RegisterVendedorForm
from users.models.Usuario import Usuario


from users.models.Vendedor import Vendedor

class RegisterVendedorView(LoginRequiredMixin ,CreateView):
    template_name = 'users/pages/register-vendedor.html'
    model = Vendedor
    form_class= RegisterVendedorForm

    def form_valid(self, form):
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.is_vendedor = True
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Agora você é um vendedor')
        return reverse('app:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_da_pagina'] = "Cadastrar vendedor"
        return context