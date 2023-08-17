from django.db import models
from django.contrib.auth.models import User


# Create your models here.
priority_choices = (
    ('High Priority','High Priority'),
    ('Medium Priority','Medium Priority'),
    ('Low Priority','Low Priority'),
)

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100,null=False,blank=False)
    priority = models.CharField(max_length=30,choices=priority_choices,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.description
    
    
    

