from django.db import models

from categories.models import CategoryJoin

class Product(models.Model):
    category_join = models.ForeignKey(CategoryJoin, on_delete=models.CASCADE)
    name          = models.CharField(max_length=50)
    product_group = models.ForeignKey('ProductGroup', on_delete=models.CASCADE)
    price         = models.DecimalField(decimal_places=2, max_digits=6)
    ml            = models.IntegerField()
    description   = models.CharField(max_length=500)
    inventory     = models.IntegerField()

    class Meta:
        db_table = 'products'

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img_url = models.URLField(max_length=1000)

    class Meta:
        db_table = 'images'

class ProductGroup(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'productgroups'