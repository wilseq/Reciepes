from django.db import models


class Vegetable(models.Model):
    rec_vegetables = models.CharField(verbose_name='vegetable', max_length=100)
    rec_veg_wt = models.CharField(verbose_name='Units', max_length=50,default='kg')
    rec_veg_latest_price= models.IntegerField(verbose_name='Price', default=0)

class Ingredients(models.Model):
    rec_ingredients = models.CharField(verbose_name='ingredient', max_length=100)
    rec_ingredient_wt = models.CharField(verbose_name='Units', max_length=50,default='kg')
    rec_ingredient_price = models.IntegerField(verbose_name='Price',default=0)

class Groceries(models.Model):
    rec_groceries = models.CharField(verbose_name='groceries', max_length=100)
    rec_groceries_wt = models.CharField(verbose_name='Units', max_length=50,default='kg')
    rec_groceries_latest_price= models.IntegerField(verbose_name='Price', default=0)





