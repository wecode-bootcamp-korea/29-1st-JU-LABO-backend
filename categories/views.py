import json, csv

from django.http            import JsonResponse
from django.views           import View
# from django.core.exceptions import ValidationError 
# from django.db.models       import Q

from .models                import Category, SubCategory, CategoryJoin
# from products.models        import Product, Image, ProductGroup
# from users.models           import User, Cart

class CategoryView(View):
  def get(self,request):
    try:
      # cat = request.GET.get('cat', None)
      subcategory = SubCategory.objects.all()
      result = [i.name for i in subcategory]
      # for i in subcategory:
      #   result.append(i.name)

      return JsonResponse({'message': result}, status=200)
    except:
      return JsonResponse({'message': 'INVALID_ERROR'}, status=400)

class SubCategoryView(View):
  def get(self,request, category_id,subcategory_id):
    try:
      result = []
      categoryjoin = CategoryJoin.objects.filter(category_id = category_id, subcategory_id = subcategory_id)[0].product_set.all()

      for i in categoryjoin:
        result.append({
          'name': i.name,
          'ml'  : i.ml,
          'price': i.price,
          'categoryjoin': SubCategory.objects.get(id = i.categoryjoin.subcategory_id).name,
        })
        
#name , ml , categoryjoin, price
      return JsonResponse({'message': result}, status= 200)
    except:
      return JsonResponse({'message': 'INVALID_ERROR'}, status=400) 

# class CsvView(View):
#   def get(self,request):
#     path = 'images.csv'
#     file = open(path)
#     reader = csv.reader(file)
#     for row in reader:
#       Image.objects.create(
#         product_id = row[0],
#         image_url = row[1]
#     )

#     return JsonResponse({'message': 'success'}, status=200)

# class CsvView(View):
#   def get(self,request):
#     path = 'productgroups.csv'
#     file = open(path)
#     reader = csv.reader(file)
#     for row in reader:
#       ProductGroup.objects.create(
#         name=row[0],
#         image_url=row[1]
#     )


#     return JsonResponse({'message': 'success'}, status=200)