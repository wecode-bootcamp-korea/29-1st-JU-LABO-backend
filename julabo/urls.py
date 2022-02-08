from django.urls import path,include

# from products.views import ProductDetailView

urlpatterns = [
  path('categories', include('categories.urls')),
  path('users', include('users.urls')),
  path('products', include('products.urls')),
  path('carts', include('carts.urls')),
]
