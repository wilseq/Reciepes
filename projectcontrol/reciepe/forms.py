from django import forms
from .models import Vegetable, Ingredients, Groceries

class RawVegetableForm(forms.ModelForm):
    class Meta:
        model = Vegetable
        fields = [
            'rec_vegetables',
            'rec_veg_wt',
            'rec_veg_latest_price',
        ]
        #rec_vegetables = forms.CharField(label='Vegetables')
        #rec_veg_wt = forms.CharField(label='Units')
        #rec_veg_latest_price = forms.IntegerField(label='Price')

class RawIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = [
            'rec_ingredients',
            'rec_ingredient_wt',
            'rec_ingredient_price',
        ]

class RawGroceriesForm(forms.ModelForm):
    class Meta:
        model = Groceries
        fields = [
            'rec_groceries',
            'rec_groceries_wt',
            'rec_groceries_latest_price',
    ]

