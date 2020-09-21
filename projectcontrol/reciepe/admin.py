from django.contrib import admin
from reciepe.models import Vegetable, Ingredients, Groceries

# Register your models here.
admin.site.register(Vegetable)
admin.site.register(Ingredients)
admin.site.register(Groceries)
