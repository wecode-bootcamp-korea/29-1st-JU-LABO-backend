from django.urls import path

from products.views      import ProductGroupDetailView

urlpatterns = {
  path('/<int:product_id>', ProductGroupDetailView.as_view()),
}
