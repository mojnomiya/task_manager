from django.urls import path
from .views import HomeView, RegisterView, LoginView, LogoutView, AddTaskView, ViewTaskView, UpdateTaskView, MarkTaskCompleteView, CompletedTasksView, TaskDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('tasks/add/', AddTaskView.as_view(), name='add_task'),
    path('tasks/<int:task_id>/', ViewTaskView.as_view(), name='view_task'),
    path('tasks/<int:task_id>/edit/', UpdateTaskView.as_view(), name='edit_task'),
    path('tasks/mark-completed/<int:task_id>', MarkTaskCompleteView.as_view(), name='mark-complete'),
    path('tasks/completed-tasks/', CompletedTasksView.as_view(), name='completed-tasks'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),

]
