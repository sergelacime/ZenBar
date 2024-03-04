from django import forms
from common.models import *

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProduitForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control text-dark border-dark'})
            