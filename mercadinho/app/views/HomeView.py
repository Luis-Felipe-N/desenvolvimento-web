from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render
from mercado.models.Produto import Produto

# Dá para usar o TemplateView, não vou usar porqus estou aprendendo
class HomeView(ListView):
    template_name = 'mercado/pages/home.html'
    context_object_name = "produtos"
    model = Produto
    
    def get_queryset(self):
        return super().get_queryset().filter(is_ativo=True)

    # def get_template(self, context):
    #     try:
    #         print(self.request.user.is_vendedor)
    #     except:
    #         print('não tem vendedor aqui')

    #     return render(self.request, self.template_name, context)

    # def get(self, request):

    #     user = request.user

    #     produtos = Produto.objects.all()

    #     context = {
    #         'user': user,
    #         'produtos': produtos
    #     }

    #     return self.get_template(context)
        