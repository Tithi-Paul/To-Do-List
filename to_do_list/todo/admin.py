from django.contrib import admin
from todo.models import TaskModel

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'taskTitle', 'is_completed')

admin.site.register(TaskModel, TaskModelAdmin)
# Register your models here.
