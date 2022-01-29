from django.urls import path

from products.views      import ProductGroupDetailView
urlpatterns = {
  path('', ProductGroupDetailView.as_view()),
}
