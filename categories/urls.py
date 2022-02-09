from django.urls import path

from .views      import SubCategoriesView         
urlpatterns = {
  path('/subcategory', SubCategoriesView.as_view()),
}
