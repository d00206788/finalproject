from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    # setting the one to many relationship, where one user can have many items. If user is deleted, tasks are also deleted
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True) 
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    # automatically populate field when created with the date and time, hence true
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title
    
    # setting complete data to be at bottom of the list
    class Meta:
        ordering = ['complete']





