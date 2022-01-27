import json, csv

from django.http            import JsonResponse
from django.views           import View

from .models                import Category, SubCategory, CategoryJoin

class SubCategoryView(View):
  def get(self,request):
    try:
      category_id    = request.GET.get('category_id', None)
      subcategory_id = request.GET.get('subcategory_id', None)

      if not CategoryJoin.objects.filter(category_id = category_id, subcategory_id = subcategory_id).exists():
        return JsonResponse({'message':'INVALID_CATEGORY'}, status=400)

      result = [{
        'name'        : category.name,
        'ml'          : category.ml,
        'price'       : category.price,
        'categoryjoin': SubCategory.objects.get(id = category.categoryjoin.subcategory_id).name
      } for category in CategoryJoin.objects.filter(category_id = category_id, subcategory_id = subcategory_id)[0].product_set.all()]

      return JsonResponse({'result': result}, status= 200)

    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400) 



