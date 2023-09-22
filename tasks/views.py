from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View

# Create your views here.
class HomeView(TemplateView):
    template_name = 'tasks/index.html'

class RegisterView(TemplateView):
    template_name = 'tasks/register.html'

class LoginView(TemplateView):
    template_name = 'tasks/login.html'