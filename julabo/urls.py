from django.urls import path

from products.views import ProductDetailView

urlpatterns = [
    path('products', ProductDetailView.as_view()),
]