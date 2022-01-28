import json, csv

from django.http            import JsonResponse
from django.views           import View

from .models                import Category, SubCategory, CategorySubCategory

class ProductListView(View):
  def get(self,request):
    try:
      category_id    = request.GET.get('category_id', None)
      subcategory_id = request.GET.get('subcategory_id', None)

      if not CategorySubCategory.objects.filter(category_id = category_id, subcategory_id = subcategory_id).exists():
        return JsonResponse({'message':'INVALID_CATEGORY'}, status=400)

      ProductList = [{
        'id'          : product.id,
        'name'        : product.name,
        'ml'          : product.ml,
        'price'       : product.price,
        'categoryjoin': SubCategory.objects.get(id = product.categoryjoin.subcategory_id).name
      } for product in CategorySubCategory.objects.filter(category_id = category_id, subcategory_id = subcategory_id)[0].product_set.all()]

      return JsonResponse({'productlist': ProductList}, status= 200)

    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400) 



