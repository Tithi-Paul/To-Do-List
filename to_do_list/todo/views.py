from django.shortcuts import render, redirect
from todo.forms import TaskForm
from todo.models import TaskModel

def showTasks(request):
    task = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'data': task})

def createTasks(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('show-tasks')
    else:
        task = TaskForm()
    
    return render(request, 'create_tasks.html', {'form': task})

def editTasks(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show-tasks')

    return render(request, 'edit_tasks.html', {'form': form})

def deleteTasks(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('show-tasks')

def completedTasks(request):
    task = TaskModel.objects.all()
    return render(request, 'completed_tasks.html', {'data': task})

def completeTask(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('completed-tasks')