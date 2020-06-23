from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm

from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks':tasks})


def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        Task.objects.create(**form.cleaned_data)
        form = TaskForm()
        return redirect('../tasks/')

    context = {
        'form': form
    }
    return render(request, 'create_task.html', context)


def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskForm(request.POST or None, instance=task)

    if task_form.is_valid():
        print('Printing POST:', request.POST)
        task_form.save()
        return redirect('../../')
    return render(request, 'create_task.html', {'form': task_form})


def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        'task': task
    }
    return render(request, 'task_detail.html', context)


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method =='POST':
        task.delete()
        return redirect('../../')
    context = {
        "task": task
    }
    return render(request, 'delete_task.html', context)
