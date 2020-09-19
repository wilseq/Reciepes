from django.db import models


class Vegetable(models.Model):
    rec_vegetables = models.CharField(max_length=100)
    rec_veg_wt = models.CharField(max_length=50,default='kg')
    rec_veg_latest_price= models.IntegerField(default=0)





