# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    # use built-in user creation form template
    form_class = UserCreationForm
    # load urls later if available because all generic class-based views the urls are not loaded when the file is imported
    success_url = reverse_lazy("login")
    # use registration/signup.html in root templates folder
    template_name = "registration/signup.html"
