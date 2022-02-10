from django.views          import View
from django.http           import JsonResponse

from .models               import Product, Image
from django.db.models      import Count

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

class ProductSearchView(View):
    def get(self,request):
      try:
        keywords            = request.GET.get('keywords', None)
        products            = Product.objects.filter(name__icontains = keywords).select_related('categorysubcategory__subcategory')
        popular_products = UserProduct.objects.values('product_id').annotate(count=Count('id')).order_by('-count')
        popular_products_id = UserProduct.objects.annotate(count=Count('id')).order_by('-count')
        # popular_products    = Product.objects.filter(id__in =[product['product_id'] for product in popular_products_id])
        
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

        popular_products = [{   
        'id'             : popular_product.product.id,
        'name'           : popular_product.product.name,
        'ml'             : popular_product.product.ml,
        'price'          : popular_product.product.price,
        'productgroup_id': popular_product.product.productgroup.id,
        'image'          : [image.image_url for image in popular_product.product.image_set.all()],
        'subcategory': {
          'subcategory_id'  : popular_product.product.categorysubcategory.subcategory.id,
          'subcategory_name': popular_product.product.categorysubcategory.subcategory.name
          }
        } for popular_product in popular_products_id]

        popular_products_info = [popular_product for popular_product in popular_products]

        # popular_products = [{'product_id': [product.name for product in popular_product.product_set.all()]}for popular_product in popular_products_id]

      


        return JsonResponse({'products': products , 'popular_products': popular_products, 'popular_products_info' : popular_products_info}, status=200)
      except:
        return JsonResponse({'message': 'KEY_ERROR'}, status=400)