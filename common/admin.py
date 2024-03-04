from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Casier)
admin.site.register(Produit)
admin.site.register(EntreStock)
admin.site.register(LigneSortie)
admin.site.register(SortieStock)
admin.site.register(Table)
admin.site.register(LigneVente)
admin.site.register(Vente)