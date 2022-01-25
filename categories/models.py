from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class Sub_Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sub_categories'

class Category_Join(models.Model):
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'category_joins'