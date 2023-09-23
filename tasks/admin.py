from django.contrib import admin
from .models import Tasks

class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'due_date', 'priority', 'is_complete')
    list_filter = ('priority', 'is_complete')
    search_fields = ('title', 'description')
    ordering = ('priority',)

admin.site.register(Tasks, TasksAdmin)
