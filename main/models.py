from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    
    PRIORITY_CHOICE = [
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICE, default=MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)
    due_time = models.TimeField(blank=True, null=True)
    tags = models.CharField(max_length=225, blank=True)
    
    def __str__(self):
        return f"{self.title}({self.get_priority_display()})"