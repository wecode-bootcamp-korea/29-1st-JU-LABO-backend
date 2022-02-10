from django.urls import path

from products.views      import ProductDetailView, ProductListView

urlpatterns = {
  path('/productlist', ProductListView.as_view()),
  path('/<int:product_id>', ProductDetailView.as_view()),
<<<<<<< HEAD
}
=======
}
>>>>>>> 975f2dd2322276067e6c3fa640b6372d3b7810ad
