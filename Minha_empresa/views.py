from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Produto
# Create your views here.


class Index(ListView):
    model = Produto
    template_name = "index/index.html"
    context_object_name = "Produtos"    