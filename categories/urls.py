from django.urls import path

<<<<<<< HEAD
from .views      import SubCategoriesView         
=======
from .views      import SubCategoriesView

>>>>>>> c71405cbf8665fabb85974d61d0a1dd3b353c687
urlpatterns = {
  path('/subcategory', SubCategoriesView.as_view()),
}
