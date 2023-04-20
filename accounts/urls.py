# accounts/urls.py
from django.urls import path

from .views import SignUpView

# route accounts url to signup/ url path and load class SignUpView as a view
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]