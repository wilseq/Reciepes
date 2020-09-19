from django.shortcuts import render
from .models import Vegetable
from .forms import RawVegetableForm
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
    my_form = RawVegetableForm()
    context = {
        "form": my_form
    }
    return render(request,'reciepe/vegetable.html', context)

def ingredients(request):
    return render(request,'reciepe/ingredients.html', {})

def groceries(request):
    return render(request,'reciepe/groceries.html', {})

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





