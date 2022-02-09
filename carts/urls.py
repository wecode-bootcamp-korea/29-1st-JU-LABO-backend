from django.urls import path

from .views      import CartView, CartRecommendView

urlpatterns = {
  path('', CartView.as_view()),
  path('/<int:cart_id>', CartView.as_view()),
  path('/recommendation', CartRecommendView.as_view()),
}