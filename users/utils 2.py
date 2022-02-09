import jwt, json

from django.http                import JsonResponse
from django.conf                import settings					
from users.models               import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers: 
            return JsonResponse ({'message' : 'UNAUTHORIZED'}, status=401)
        try:
            access_token = request.headers.get('Authorization')
            payload = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
            user = User.objects.get(id=payload['id'])
            request.users = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'} , status = 400)
        
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'},status=401)
        
        return func(self, request, *args, **kwargs)
    
    return wrapper 