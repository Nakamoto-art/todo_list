from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm

from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks':tasks})

# def create_task(request):
#     form = TaskForm()
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Task.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors )

#     context = {
#         'form': form
#     }
#     return render(request, 'create_task.html', context)

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

def update_task(request):
    pass

def task_list_view(request):
    queryset = Task.objects.all()
    context = {
        'task_list': queryset
    }
    return render(request, 'task_list.html', context)