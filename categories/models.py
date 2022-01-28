from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class SubCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'subcategories'

class CategorySubCategory(models.Model):
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory  = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categorysubcategories'