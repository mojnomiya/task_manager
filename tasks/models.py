from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    photos = models.ImageField(blank=True, upload_to='static/task_photos/')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

