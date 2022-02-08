import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import F, Count

from users.models     import Cart, User
from products.models  import Product
from users.utils      import login_decorator

class CartView(View):
    @login_decorator
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user_id    = request.user.id
            product_id = data['product_id']
            quantity   = data['quantity']

            cart, is_created = Cart.objects.get_or_create(
                user_id=user_id, product_id=product_id)

            cart.quantity = F('quantity') + quantity
            cart.save()
    
 
            return JsonResponse({'message': 'Success'}, status=200)
        except KeyError:
            return JsonResponse({'message': 'Key Error'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User id Does Not Exist'}, status=400)

    @login_decorator
    def get(self, request):
        user = request.user
        try:
            carts = Cart.objects.filter(user_id=request.user.id)
            
            results = [
                {
                    'product_name' : cart.product.name,
                    'quantity'     : cart.quantity,
                    'item_price'   : cart.product.price * cart.quantity,
                    'price'        : cart.product.price,
                    'subcategory'  : cart.product.categorysubcategory.subcategory.name,
                    'size'         : cart.product.ml,
                    'cart_id'      : cart.id,
                    'image_url'    : cart.product.image_set.all()[0].image_url,
                    'product_id'   : cart.product.id
                } 
                for cart in carts]

            total_price = 0

            for result in results:
                total_price += result['item_price']

            return JsonResponse({'results': results, 'total_price': total_price}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

    @login_decorator
    def delete(self, request, cart_id):
        Cart.objects.filter(user_id=request.user.id, id=cart_id).delete()
        return JsonResponse({'message': 'No content'}, status=204)

    @login_decorator
    def put(self, request):
        user_id  = request.user.id
        data     = json.loads(request.body)
        cart_id  = data['cart_id']
        quantity = data['quantity']

        cart = Cart.objects.filter(user_id=user_id, id=cart_id)
        cart.update(quantity=quantity)

        return JsonResponse({'message': 'Success'}, status=201)


class CartRecommendView(View):
    @login_decorator
    def get(self, request):
        try:
            carts = Cart.objects.filter(user_id=request.user.id)
            product_ids = [cart.product_id for cart in carts]
            field_name = 'product_id__categorysubcategory'
            results = carts.values(field_name).annotate(count=Count('product_id')).order_by('-count')
            most_popular_id = results[0][field_name]

            recommendation_products = Product.objects.filter(categorysubcategory_id=most_popular_id).exclude(id__in=product_ids).filter(is_default=True)

            results = [
                {
                    'product_name' : product.name,
                    'price'        : product.price,
                    'subcategory'  : product.categorysubcategory.subcategory.name,
                    'size'         : product.ml,
                    'product_id'   : product.id,
                    'image_url'    : product.image_set.all()[0].image_url,
                    'season'       : product.categorysubcategory.category.name
                } for product in recommendation_products]

            return JsonResponse({'results': results}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'Key Error'}, status=400)