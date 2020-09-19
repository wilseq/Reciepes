from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('about/',views.about, name = 'about'),
    path('contact/',views.contact, name = 'contact'),
    path('blog/',views.blog, name = 'blog'),
    path('price/',views.price, name = 'price'),
    path('vendor/',views.vendor, name='vendor'),
    path('vegetable/',views.vegetable, name='vegetable'),
    path('ingredients/',views.ingredients, name='ingredients'),
    path('groceries/',views.groceries, name='groceries'),
    path('menu/',views.menu, name='menu'),
    path('button6/',views.button6, name='button6'),
    path('button7/',views.button7, name='button7'),
    path('button8/',views.button8, name='button8'),
    path('button9/',views.button9, name='button9'),
]