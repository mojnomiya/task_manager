from django.urls import path
from .views import HomeView, RegisterView, LoginView, LogoutView, AddTaskView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('tasks/add/', AddTaskView.as_view(), name='add_task'),
]
