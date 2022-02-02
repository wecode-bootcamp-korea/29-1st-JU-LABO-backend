from django.urls import path

from products.views      import ProductGroupDetailView

urlpatterns = {
  path('/<int:productgroup_id>', ProductGroupDetailView.as_view()),
}
