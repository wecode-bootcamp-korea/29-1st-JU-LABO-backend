from django.urls import path,include

# from products.views import ProductDetailView
from users.views import CartView

urlpatterns = [
  path('categories', include('categories.urls')),
  path('users', include('users.urls')),
  path('cart', CartView.as_view()),
  path('productgroups', include('products.urls')),
]
