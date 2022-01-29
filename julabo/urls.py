from django.urls import path,include

urlpatterns = [
  path('categories', include('categories.urls')),
  path('productgroups', include('products.urls')),
]
