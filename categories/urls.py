from django.urls import path

from .views      import CategoryView, SubCategoryView

urlpatterns = {
  path('category', CategoryView.as_view()),
  path('subcategory/<int:category_id>/<int:subcategory_id>', SubCategoryView.as_view()),
  # path('csv', CsvView.as_view())
}