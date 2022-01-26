from django.db import models

from categories.models import CategoryJoin

class Product(models.Model):
    categoryjoin  = models.ForeignKey(CategoryJoin, on_delete=models.CASCADE)
    name          = models.CharField(max_length=50)
    productgroup  = models.ForeignKey('ProductGroup', on_delete=models.CASCADE)
    price         = models.DecimalField(decimal_places=2, max_digits=6)
    ml            = models.IntegerField()
    description   = models.CharField(max_length=500)
    inventory     = models.IntegerField()
    is_default    = models.BooleanField(default=False)

    class Meta:
        db_table = 'products'

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=1000)

    class Meta:
        db_table = 'images'

class ProductGroup(models.Model):
    name    = models.CharField(max_length=50)
    image_url = models.URLField(max_length=1000)
    

    class Meta:
        db_table = 'productgroups'