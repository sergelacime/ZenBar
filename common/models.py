from django.db import models


class Casier(models.Model):
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    prix_achat_casier = models.FloatField()
    nombre_casier = models.IntegerField(default=1)
    seuil = models.IntegerField(default=10)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_edit = models.DateTimeField(auto_now_add=True)


class Produit(models.Model):
    libelle = models.CharField(max_length=50)
    prix_vente = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_edit = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.libelle)


class EntreStock(models.Model):
    casiers = models.ManyToManyField("Casier")
    prix_stock = models.FloatField()
    remise = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_edit = models.DateTimeField(auto_now_add=True)


class LigneSortie(models.Model):
    casier = models.ForeignKey("casier", on_delete=models.CASCADE)
    nombre = models.IntegerField()


class SortieStock(models.Model):
    casiers = models.ManyToManyField("LigneSortie")
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_edit = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Table(models.Model):
    items = (
        ("Occuper","Occuper"),
        ("Libre","Libre")
    )
    
    code = models.CharField(max_length=10)
    statut = models.CharField(choices=items, max_length=10, default="Libre")
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_edit = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Table " + str(self.code)


class LigneVente(models.Model):
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)


class Vente(models.Model):
    items = (
        ("Impayer","Impayer"),
        ("Payer","Payer")
    )
    table = models.ForeignKey("Table", on_delete=models.CASCADE)
    lignes = models.ManyToManyField("LigneVente")
    total = models.FloatField()
    remise = models.FloatField()
    statut = models.CharField(choices=items, max_length=10, default="Impayer")
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_edit = models.DateTimeField(auto_now_add=True)