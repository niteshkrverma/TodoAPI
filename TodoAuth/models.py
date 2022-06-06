from django.db import models

# Create your models here.
class Todo(models.Model): #create todo database where we store all todo data
    Title=models.CharField(max_length=100,blank=False) 
    Description=models.TextField(blank=False)
    Date=models.DateField(blank=False)
    Completed=models.BooleanField(default=False)
    def __str__(self):
        return self.Title

