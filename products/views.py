from django.views import View
from django.http  import JsonResponse

from .models      import Product, Image

class ProductGroupDetailView(View):
    def get(self, request, product_id):
        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({'message':'product_id error'}, status=400)
            
        productgroup_id = Product.objects.get(id=product_id).productgroup_id
        product         = Product.objects.filter(id=product_id)
        other_products  = Product.objects.filter(productgroup_id=productgroup_id).exclude(id=product_id)
        products        = product.union(other_products)

        results = [
            {
                'product_id'         : product.id,
                'name'               : product.name,
                'category'           : product.categorysubcategory.category.name,
                'subcategory'        : product.categorysubcategory.subcategory.name,
                'ml'                 : product.ml,
                'price'              : product.price,
                'description'        : product.description,
                'image_urls'         : [image.image_url for image in Image.objects.filter(product_id=product.id)],
                'image_descriptions' : [
                    image.image_url.split('/')[-1].split('.')[0] 
                for image in Image.objects.filter(product_id=product.id)
                ]
            } for product in products
        ]
        mls    = sorted([result['ml'] for result in results])
        prices = sorted([result['price'] for result in results])
        return JsonResponse({'products': results, 'mls': mls, 'prices': prices}, status=200)

class ProductListView(View):
  def get(self,request):
    try:
      category_subcategory_id = request.GET.get('category_subcategory_id', None)
      type_ml                 = request.GET.get('ml', None)
      
      filter_set = {}

      if category_subcategory_id:
          filter_set["categorysubcategory_id"] = category_subcategory_id

      if type_ml:
          filter_set["ml"] = type_ml
      
      products = Product.objects.filter(**filter_set) 
      
      products = [{   
        'id'             : product.id,
        'name'           : product.name,
        'ml'             : product.ml,
        'price'          : product.price,
        'productgroup_id': product.productgroup.id,
        'image'          : [image.image_url for image in product.image_set.all()],
        'subcategory': {
          'subcategory_id'  : product.categorysubcategory.subcategory.id,
          'subcategory_name': product.categorysubcategory.subcategory.name
        }
      } for product in products]

      return JsonResponse({'products': products}, status= 200)

    except KeyError:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400)