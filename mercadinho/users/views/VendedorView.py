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
    # success_url = redirect('mercado:home')

    # def dispatch(self, request, *args, **kwargs):
    #     usuario_vendedor = hasattr(self.request.user, '')
    #     if usuario_vendedor:
    #         messages.error(self.request, 'Usuário já é vendedor')
    #         return redirect('mercado:home')
    #     return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self, form):
        usuario = Usuario.objects.get(id=self.request.user.id)
        usuario.is_vendedor = True
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Agora você é um vendedor')
        return reverse('mercado:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_da_pagina'] = "Cadastrar vendedor"
        return context
        

    # def get_template(self, form):

    #     context = {
    #         "form": form
    #     }

    #     return render(self.request, self.template_name, context)

    # def get(self, request, *args, **kwargs):
    #     form = RegisterVendedorForm()

    #     return self.get_template(form)

    # def post(self, request, *args, **kwargs):
        
    #     form = RegisterVendedorForm(request.POST)

    #     if form.is_valid():
    #         vendedor = form.save(commit=False)

    #         vendedor.username = request.user

    #         vendedor.username.is_vendedor = True

    #         form.save()

    #         return redirect('mercado:home')

    #     return self.get_template(form)