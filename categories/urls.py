from django.urls import path

from .views      import ProductListView

urlpatterns = {
    path('/productview', ProductListView.as_view()),
}
