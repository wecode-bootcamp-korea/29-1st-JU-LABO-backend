import json, re , bcrypt, jwt 

from django.http            import JsonResponse
from django.views           import View


from users.models           import User, UserProduct
from products.models        import Product

from django.conf            import settings
from users.utils            import login_decorator

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

            
            if not re.match(REGEX_EMAIL , email):
                return JsonResponse({"message" : "INVALID_EMAIL"}, status = 400)

            if not re.match(REGEX_PASSWORD , password):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'EMAIL_ALREADY_EXISTS'}, status=400)    

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
            data  = json.loads(request.body) 
            user  = User.objects.get(email=data['email'])
                
            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status = 401)
                
                return JsonResponse({'message':'SUCCESS','token':token}, status=201)
                  
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)        


class PopularProductView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(id = data['user_id'])
            product = Product.objects.get(id = data['product_id'])

            userproduct, is_userproduct = UserProduct.objects.get_or_create(
               user_id = user.id,
               product_id = product.id
            )

            if not is_userproduct:
                return JsonResponse({'message': '이미 눌렸습니다'}, status=200)

            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message': "INVALID_USER"}, status = 404)

        except Product.DoesNotExist:    
            return JsonResponse({'message': "INVALID_PRODUCT"}, status = 404)     

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)