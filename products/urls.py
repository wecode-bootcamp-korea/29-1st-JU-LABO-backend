from django.urls import path

from products.views      import ProductGroupDetailView, ProductListView

urlpatterns = {
  path('/productlist', ProductListView.as_view()),
  path('/<int:productgroup_id>', ProductGroupDetailView.as_view()),
}
