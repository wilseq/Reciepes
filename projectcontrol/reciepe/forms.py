from django import forms
from .models import Vegetable

class RawVegetableForm(forms.Form):
    rec_vegetables = forms.CharField()
    rec_veg_wt = forms.CharField()
    rec_veg_latest_price = forms.IntegerField()