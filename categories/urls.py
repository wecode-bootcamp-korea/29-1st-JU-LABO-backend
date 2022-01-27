from django.urls import path

from .views      import SubCategoryView

urlpatterns = {
  path('/subcategory', SubCategoryView.as_view()),
}