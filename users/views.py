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
                
            )

            return JsonResponse({'message':'SUCCESS'},status=200)
    
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=401)

class LogInView(View):
    def post(self,request):
        data = json.loads(request.body) 
        try: 
            if not User.objects.filter(
                email    = data['email'],
                password = data['password'],
                ).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            if bcrypt.checkpw(data['password'].encode('utf-8'), User.password.encode('utf-8')):
                token = jwt.encode({'id': User.id}, SECRET_KEY, algorithm=ALGORITHM)
                return JsonResponse({'token':token}, status=200)

            return JsonResponse({'message':'SUCCESS'},status=200) 

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)            




