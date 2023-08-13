from django.db import models

class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)

