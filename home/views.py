from django.shortcuts import render, redirect
from common.models import *
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from .forms import *

# Create your views here.
class Index(TemplateView):
    template_name = "pages/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all().order_by("-statut")
        return context


class TableView(ListView):
    model = Table
    context_object_name = "tables"
    template_name = "pages/tables.html"
    
    def post(self, request, *args, **kwargs):
        code = request.POST.get("code")
        Table.objects.create(code=code)
        #messages.success(request,"succès")
        return redirect("tables")
  

class StockView(ListView):
    model = Produit
    content_type_name = "produits"
    template_name = "pages/stock.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProduitForm()
        context["produits"] = Produit.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ProduitForm(request.POST)
        form.save()
        #messages.success(request,"succès")
        return redirect("stock")


class StockEntries(TemplateView):
    template_name = "pages/entries.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produits"] = Produit.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        #messages.success(request,"succès")
        return redirect("entries")