from django.http            import JsonResponse
from django.views           import View

from products.models        import Product,Image
from .models                import SubCategory

class SubCategoriesView(View):
  def get(self,request):

    sub_categories = [{
      'id'  : sub_category.id,
      'name': sub_category.name
    } for sub_category in SubCategory.objects.all()]

    return JsonResponse({'sub_categories': sub_categories}, status=200)


class ProductListView(View):
  def get(self,request):
    try:
      category_subcategory_id    = request.GET.get('category_subcategory_id', None)

      products = Product.objects.filter(categorysubcategory__id = category_subcategory_id)
      image = Image.objects.all()
      products = [{
        'id'          : product.id,
        'name'        : product.name,
        'ml'          : product.ml,
        'price'       : product.price,
        'image':{
          'img1': image.filter(product_id= product.id).values('image_url')[0],
          'img2': image.filter(product_id= product.id).values('image_url')[1],
          'img3': image.filter(product_id= product.id).values('image_url')[2]
        },
        'subcategory': {
          'subcategory_id'  : product.categorysubcategory.subcategory.id,
          'subcategory_name': product.categorysubcategory.subcategory.name
        }
      } for product in products]

      return JsonResponse({'products': products}, status= 200)

    except:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400) 




