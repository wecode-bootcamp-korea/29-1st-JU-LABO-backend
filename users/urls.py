from django.urls import path
from .views      import SignUpView, LogInView, PopularProductView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login',  LogInView.as_view()),
    path('/popular', PopularProductView.as_view())
]