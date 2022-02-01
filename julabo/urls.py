from django.urls import path,include

# from products.views import ProductDetailView
from users.views import CartView

urlpatterns = [
    # path('products', ProductDetailView.as_view())
    path('cart', CartView.as_view())
]