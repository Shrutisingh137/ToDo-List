from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Task

def task_list_view(request):
    task_list = Task.objects.all().order_by('-created_at')
    total_tasks = task_list.count()

    paginator = Paginator(task_list, 10)
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    return render(
        request,
        'tasks/task_list.html',
        {
            'tasks': tasks,
            'total_tasks': total_tasks
        }
    )


def welcome_view(request):
    return render(request, 'tasks/welcome.html')

