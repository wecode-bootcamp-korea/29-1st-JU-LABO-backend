from django.views import View
from django.http import JsonResponse

from .models import Product, Image

class ProductGroupDetailView(View):
    def get(self, request, product_id): #TODO: productgroup_id 받기
        if not Product.objects.filter(productgroup_id=product_id).exists():
            return JsonResponse({'message':'productgroup_id error'}, status=400)

        try:
            products = Product.objects.filter(productgroup_id=product_id).order_by('is_default')

            results = [
                {
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
            mls    = [result['ml'] for result in results]
            prices = [result['price'] for result in results]
            return JsonResponse({'products': results, 'mls': mls, 'prices': prices}, status=200)
        except IndexError: # TODO: except 별로 작성하기
            return JsonResponse({'message': 'Index Error'}, status=400)