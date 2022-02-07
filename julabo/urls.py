from django.urls import path,include

urlpatterns = [
  path('categories', include('categories.urls')),
  path('users', include('users.urls')),
  path('products', include('products.urls')),
]
