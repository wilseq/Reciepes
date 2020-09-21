from django.shortcuts import render
from .models import Vegetable
from .forms import RawVegetableForm, RawIngredientForm, RawGroceriesForm
# Create your views here.
def index(request):

    #context = {'reciepe_vegetables': Banana }
    #context ='This is an index page'
    return render(request,'reciepe/index.html', {})

def about(request):

    #context = {'reciepe_vegetables': Banana }
    #context ='This is an index page'
    return render(request,'reciepe/about.html', {})

def contact(request):

    #context = {'reciepe_vegetables': Banana }
    #context ='This is an index page'
    return render(request,'reciepe/contact.html', {})

def blog(request):
    return render(request,'reciepe/blog.html', {})

def price(request):

    #context = {'reciepe_vegetables': Banana }
    #context ='This is an index page'
    return render(request,'reciepe/price.html', {})

def vendor(request):
    return render(request,'reciepe/vendor.html', {})

def vegetable(request):
    my_form = RawVegetableForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = RawVegetableForm()
    context = {
        "form": my_form
    }
    return render(request,'reciepe/vegetable.html', context)

def ingredients(request):
    ingredients_form = RawIngredientForm(request.POST or None)
    if ingredients_form.is_valid():
        ingredients_form.save()
        ingredients_form = RawIngredientForm()
    context = {
        "form": ingredients_form
    }
    return render(request,'reciepe/ingredients.html', context)

def  groceries(request):
    my_form = RawGroceriesForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = RawGroceriesForm()
    context = {
        "form": my_form
    }
    return render(request,'reciepe/groceries.html', context)

def menu(request):
    return render(request,'reciepe/menu.html', {})

def button6(request):
    return render(request,'reciepe/button6.html', {})

def button7(request):
    return render(request,'reciepe/button7.html', {})

def button8(request):
    return render(request,'reciepe/button8.html', {})

def button9(request):
    return render(request,'reciepe/button9.html', {})





