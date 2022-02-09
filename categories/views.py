import json 

from django.http            import JsonResponse
from django.views           import View

from .models                import SubCategory
from users.models           import User
from products.models        import Product

class SubCategoriesView(View):
  def get(self,request):

    sub_categories = [{
      'id'  : sub_category.id,
      'name': sub_category.name
    } for sub_category in SubCategory.objects.all()]

    return JsonResponse({'sub_categories': sub_categories}, status=200)