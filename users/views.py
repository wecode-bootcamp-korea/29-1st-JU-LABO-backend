from itertools import product
import json

from django.views import View
from django.http  import JsonResponse
from django.db.models import F

from users.models import User, Cart

class CartView(View):
    def post(self, request):
        data = json.loads(request.body)

        user_id = data['user_id']
        product_id = data['product_id']
        quantity = data['quantity']

        cart, is_created = Cart.objects.get_or_create(user_id=user_id, product_id=product_id)
        
        if not is_created:
            cart.quantity = F('quantity') + quantity
        
        else:
            cart.quantity = quantity
        
        cart.save()
        
        return JsonResponse({'message': '등록성공'}, status=200)


        