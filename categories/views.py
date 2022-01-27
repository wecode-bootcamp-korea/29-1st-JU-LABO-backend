import json, csv

from django.http            import JsonResponse
from django.views           import View

from .models                import Category, SubCategory, CategoryJoin

class CategoryView(View):
  def get(self,request):

    sub_categories = [{
      'id'  : sub_category.id,
      'name': sub_category.name
    } for sub_category in SubCategory.objects.all()]

    return JsonResponse({'sub_categories': sub_categories}, status=200)

class SubCategoryView(View):
  def get(self,request, category_id,subcategory_id):
    try:
      if not CategoryJoin.objects.filter(category_id = category_id, subcategory_id = subcategory_id).exists():
        return JsonResponse({'message':'INVALID_CATEGORY'}, status=400)

      result = [{
        'name' : category.name,
        'ml'   : category.ml,
        'price': category.price,
        'categoryjoin': SubCategory.objects.get(id = category.categoryjoin.subcategory_id).name
      } for category in CategoryJoin.objects.filter(category_id = category_id, subcategory_id = subcategory_id)[0].product_set.all()]

        
      return JsonResponse({'result': result}, status= 200)
    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400) 

class TypeView(View):
  def get(self,request):
    return JsonResponse({'message':'SUCCESS'}, status=200)

