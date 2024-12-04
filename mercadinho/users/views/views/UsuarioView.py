from multiprocessing import context
from django.forms import ValidationError
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms.UsuarioForm import RegisterUsuarioForm, LoginForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView as LoginViewClass

from users.models.Usuario import Usuario

# Redirecionar para home que estiver logado

class LoginView(LoginViewClass):
    template_name = 'users/pages/login.html'

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            messages.error(self.request, 'Usuário já está logado, faça logOut para entrar novamente')
            return redirect('mercado:home')
        return super().dispatch(request, *args, **kwargs)

    def get_template(self, form=None, *args, **kwargs):
        
        if form is None:
            form = LoginForm()

        context = {
            'form': form,
            "titulo_da_pagina": "Entrar no mercadinho"
        }
        
        return render(self.request, self.template_name, context)

    def get(self, request):
        return self.get_template()

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login feito com sucesso')
                return redirect(reverse('mercado:home'))
            else:
                messages.error(request, "Usuário ou senha inválida")
                return self.get_template(form)
        else:
            return self.get_template(form)

class LogoutView(LoginRequiredMixin, View):
    
    def get(self, request):
        logout(request)

        return redirect(reverse('mercado:home'))

class RegisterUsuarioView(View):
    template_name = 'users/pages/register.html'

    def get_template(self, form, *args, **kwargs):

        context = {
            'form': form,
            'titulo_da_pagina': "Cadastar no mercadinho"
        }
        
        return render(self.request, self.template_name, context)

    def get(self, request):
        form = RegisterUsuarioForm()
        
        return self.get_template(form)

    def post(self, request):
        form = RegisterUsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(usuario.password)
            usuario.save()
            messages.success(request, 'Conta criada com sucesso')
            return redirect(reverse('users:login'))
        else:
            return self.get_template(form)

