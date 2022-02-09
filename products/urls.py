from django.urls import path

from products.views      import ProductGroupDetailView, ProductListView

urlpatterns = {
  path('/<int:product_id>', ProductGroupDetailView.as_view()),
  path('/productlist', ProductListView.as_view())
}
