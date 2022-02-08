import json

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F

import jwt

from users.models           import Cart, User
# from users.utils            import login_decorator
from julabo.settings import SECRET_KEY, ALGORITHM

class CartView(View):
    # @login_decorator
    def post(self, request):
        try:
            access_token = request.headers.get('Authorization')
            payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            user = User.objects.get(id=payload['id'])

            data = json.loads(request.body)
            user_id = user.id
            product_id = data['product_id']
            quantity = data['quantity']

            cart, is_created = Cart.objects.get_or_create(
                user_id=user_id, product_id=product_id)

            cart.quantity = F('quantity') + quantity
            cart.save()
 
            return JsonResponse({'message': 'Success'}, status=200)
        except KeyError:
            return JsonResponse({'message': 'Key Error'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User id Does Not Exist'}, status=400)
        # except ObjectDoesNotExist:
        #     return JsonResponse({'message': 'Product id Does Not Exist'}, status=400)


    # @login_decorator
    def get(self, request):
        # user = request.user
        try:
            access_token = request.headers.get('Authorization')
            payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            user = User.objects.get(id=payload['id'])
        
            carts = Cart.objects.filter(user_id=user.id)
            
            results = [
                {
                    'product_name' : cart.product.name,
                    'quantity'     : cart.quantity,
                    'item_price'   : cart.product.price * cart.quantity,
                    'subcategory'  : cart.product.categorysubcategory.subcategory.name,
                    'size'         : cart.product.ml,
                    'cart_id '     : cart.cart_id
                } 
                for cart in carts]

            total_price = 0

            for result in results:
                total_price += result['item_price']

            return JsonResponse({'results': results, 'total_price': total_price}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'} , status = 400)
        
        except User.DoesNotExist:
            return JsonResponse({'message': 'User id Does Not Exist'}, status=400)

    # @login_decorator # 여러 제품 삭제할 시 쿼리 파라미터로 요청
    def delete(self, request,cart_id):
        access_token = request.headers.get('Authorization')
        payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
        user = User.objects.get(id=payload['id'])
        user_id = user.id

        Cart.objects.filter(user_id=user_id, cart_id=cart_id).delete()
        return JsonResponse({'message': 'No content'}, status=204)

    # @login_decorator
    def put(self, request, cart_id):
        # user = request.user
        access_token = request.headers.get('Authorization')
        payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
        user = User.objects.get(id=payload['id'])
        user_id = user.id
        data = json.loads(request.body)
        product_id = data['product_id']
        quantity = data['quantity']

        cart = Cart.objects.filter(user_id=user_id, product_id=product_id)
        cart.update(quantity=quantity)

        return JsonResponse({'message': 'Success'}, status=201)