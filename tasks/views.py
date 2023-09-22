from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .forms import UserRegForm, UserLoginForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'tasks/index.html'

class RegisterView(FormView):
    template_name = 'tasks/register.html'
    form_class = UserRegForm
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)

class LoginView(FormView):
    template_name = 'tasks/login.html'
    form_class = UserLoginForm 
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))