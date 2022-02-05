from django.http            import JsonResponse
from django.views           import View

from products.models        import Product

class ProductListView(View):
  def get(self,request):
    try:
      category_subcategory_id    = request.GET.get('category_subcategory_id', None)

      products = Product.objects.filter(categoryjoin__id = category_subcategory_id)

      products = [{
        'id'          : product.id,
        'name'        : product.name,
        'ml'          : product.ml,
        'price'       : product.price,
        'subcategory': {
        'subcategory_id'  : product.categorysubcategory.subcategory.id,
        'subcategory_name': product.categorysubcategory.subcategory.name
        }
      } for product in products]

      return JsonResponse({'products': products}, status= 200)

    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400) 




