from django.urls import path,include

urlpatterns = [
  path('categories', include('categories.urls')),
  path('users', include('users.urls')),
]