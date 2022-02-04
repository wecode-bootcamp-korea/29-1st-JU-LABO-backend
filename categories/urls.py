from django.urls import path

from .views      import ProductListView, SubCategoriesView,ProductTypeView
urlpatterns = {
  path('/product', ProductListView.as_view()),
  path('/subcategory', SubCategoriesView.as_view()),
  path('/type', ProductTypeView.as_view()),
}
