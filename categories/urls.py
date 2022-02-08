from django.urls import path

from .views      import ProductListView, SubCategoriesView

urlpatterns = {
  path('/product', ProductListView.as_view()),
  path('/subcategory', SubCategoriesView.as_view()),
}
