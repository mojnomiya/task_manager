from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .forms import UserRegForm, UserLoginForm
from .models import Tasks
from .forms import TaskForm

# Create your views here.
class HomeView(ListView):
    model = Tasks
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')
        filter_query = Q()

        if search_query:
            filter_query |= Q(title__icontains=search_query)

        priority_filter = self.request.GET.get('priority', '')
        if priority_filter:
            filter_query &= Q(priority=priority_filter)

        due_date_filter = self.request.GET.get('due_date', '')
        if due_date_filter:
            filter_query &= Q(due_date=due_date_filter)

        completion_status_filter = self.request.GET.get('is_complete', '')
        if completion_status_filter:
            filter_query &= Q(is_complete=(completion_status_filter == 'True'))

        filter_query &= Q(is_complete=False)
        return queryset.filter(filter_query)

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
    success_url = '/'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.created_by = self.request.user
        task.save()
        return super().form_valid(form)
    
class ViewTaskView(DetailView):
    model = Tasks
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'


class UpdateTaskView(UpdateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/edit_task.html'
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

    def get_success_url(self):
        return reverse('home') 
    
class MarkTaskCompleteView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Tasks, pk=task_id)
        task.is_complete = True
        task.save()
        return redirect('home') 

class CompletedTasksView(ListView):
    model = Tasks
    template_name = 'tasks/completed_tasks.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        filter_query = Q()

        if search_query:
            filter_query |= Q(title__icontains=search_query)

        completion_status_filter = self.request.GET.get('is_complete', '')
        if completion_status_filter:
            filter_query &= Q(is_complete=(completion_status_filter == 'True'))
            
        filter_query &= Q(is_complete=True)
        return queryset.filter(filter_query)
    
class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = reverse_lazy('home')
    template_name = 'tasks/task_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # You can add permission checks here if needed
        return obj