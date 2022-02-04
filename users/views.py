<<<<<<< HEAD
import json
import datetime

from django.views import View
from django.http  import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from users.models import User, Cart

class CartView(View):
    # @login_decorator
    def post(self, request):
        # user_id = request.user
        try:  
            data = json.loads(request.body)  
            user_id    = data['user_id']
            product_id = data['product_id']
            quantity   = data['quantity']

            cart, is_created = Cart.objects.get_or_create(
                user_id=user_id, product_id=product_id)

            cart.quantity = quantity
            cart.save()
            return JsonResponse({'message': '등록성공'}, status=200)
        except KeyError as k:
            return JsonResponse({'message': k}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User id Does Not Exist'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Product id Does Not Exist'}, status=400)


    # @login_decorator
    def get(self, request):

        # user_id = request.user
        try:
            user_id = 1
            
            items = Cart.objects.filter(user_id=user_id)
            
            results = [
                {
                    'product_name' : item.product.name,
                    'quantity'     : item.quantity,
                    'item_price'   : item.product.price * item.quantity,
                    'subcategory'  : item.product.categorysubcategory.subcategory.name,
                    'size'         : item.product.ml
                } 
                for item in items]

            total_price = 0
            for result in results:
                total_price += result['item_price']
            
            order_date = datetime.datetime.now()

            return JsonResponse({'results': results, 
                    'total_price': total_price, 
                    'order_date': order_date}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User id Does Not Exist'}, status=400)

    # @login_decorator
    def delete(self, request):
        # user_id = request.user
        try:
            data       = json.loads(request.body)
            user_id    = data['user_id']
            product_id = data['product_id']
            
            product = Cart.objects.get(user_id=user_id, product_id=product_id)
            product.delete()
            return JsonResponse({'message': '삭제성공'}, status=200)
        except KeyError as k:
            return JsonResponse({'message': k}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User id Does Not Exist'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Product id Does Not Exist'}, status=400)
=======
import json, re , bcrypt, jwt 

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from my_settings            import SECRET_KEY,ALGORITHM
from users.models           import User


REGEX_EMAIL = "^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
REGEX_PASSWORD = "^(?=.{8,16}$)(?=.*[a-z])(?=.*[0-9]).*$"

class SignUpView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)    
            firstname          = data['first_name']
            lastname           = data['last_name']
            email              = data['email']
            password           = data['password']


            if User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'EMAIL_ALREADY_EXISTS'}, status=400)    
            
            if not re.match(REGEX_EMAIL , email):
                return JsonResponse({"message" : "INVALID_EMAIL"}, status = 400)

            if not re.match(REGEX_PASSWORD , password):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 400)

            hashed_password = bcrypt.hashpw(data['password'].encode('UTF-8'), bcrypt.gensalt()).decode('utf-8')
            
            User.objects.create(
                first_name            = firstname,
                last_name             = lastname,
                email                 = email,
                password              = hashed_password,
                is_agree              = 'False'            
            )

            return JsonResponse({'message':'SUCCESS'},status=200)
    
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=401)

class LogInView(View):
    def post(self,request):
        try:
            data = json.loads(request.body) 
            user  = User.objects.get(email=data['email'])

            if not User.objects.filter(email = user.email).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
                
            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'id': user.id}, SECRET_KEY, ALGORITHM)
                
                return JsonResponse({'message':'SUCCESS','token':token}, status=201)
                  
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)        




>>>>>>> main
