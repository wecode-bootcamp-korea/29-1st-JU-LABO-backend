from django.urls import path,include

# from products.views import ProductDetailView
from users.views import CartView

urlpatterns = [
    # path('products', ProductDetailView.as_view())
    path('carts', CartView.as_view())
]