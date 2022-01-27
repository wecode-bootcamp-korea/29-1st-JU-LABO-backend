from django.urls import path

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login',  LogInView.as_view()),
]