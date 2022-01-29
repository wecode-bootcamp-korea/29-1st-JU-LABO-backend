from django.urls import path,include

from products.views import ProductDetailView

urlpatterns = [
    path('products', ProductDetailView.as_view())
]