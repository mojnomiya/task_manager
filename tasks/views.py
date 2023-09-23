from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView, CreateView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegForm, UserLoginForm
from .models import Tasks
from .forms import TaskForm

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
    
class AddTaskView(LoginRequiredMixin, CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/add_tasks.html'
    success_url = '/home/'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.created_by = self.request.user
        task.save()
        return super().form_valid(form)