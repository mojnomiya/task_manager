from rest_framework import generics
from .models import Tasks
from .serializers import TaskSerializer

# API Views
class TaskListCreateView(generics.ListCreateAPIView):
    """
    Can fetch all the tasks and create new tasks
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Can fetch a specific task and perform edit, delete actions
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer