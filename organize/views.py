from django.shortcuts import render
from .forms import AssetForm, TaskForm, WorkerForm
from .models import Asset, Task, Worker

def base(request):
    return render(request, 'index.html', None)


def add_asset(request):
    form = AssetForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AssetForm()

    context = {'form': form}
    return render(request, 'add_asset.html', context)

def add_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        form =TaskForm()

    context = {'form': form}
    return render(request, 'add_task.html', context)

def add_worker(request):
    form = WorkerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = WorkerForm()
    context = {'form': form}
    return render(request, 'add_worker.html', context)

def display_assets(request):
    form = AssetForm()
    assets = Asset.objects.all()
    context ={'form': form, 'assets': assets}
    return render(request, 'display_assets.html', context)

def display_tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'display_tasks.html', context)


def display_workers(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'display_workers.html', context)

