from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.shortcuts import render



def home(request):
    tasks = Task.objects.all()

    return render(request, 'home.html', {'tasks' : tasks})

def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Task created successfully')

            return redirect('home')

    return render(request, 'create_task.html', context={'form' : form})

def update_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your task has been Updated successfully.')
            return redirect('task_detail', pk=pk)

    return render(request, 'task_form.html',
                  {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.add_message(request, messages.SUCCESS, 'Your task has been deleted.')
    return redirect('home')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', context={'task' : task})