from django.urls import path
from .views_api import create_task, get_tasks, update_task, delete_task
from .views_web import task_list_view, welcome_view

urlpatterns = [

    # Web
    path('', welcome_view, name='welcome'),
    path('tasks/', task_list_view, name='task_list'),

    path('api/tasks/', get_tasks, name='get_tasks'),
    path('api/tasks/create/', create_task, name='create_task'),
    path('api/tasks/<int:task_id>/', update_task),
    path('api/tasks/<int:task_id>/delete/', delete_task)

]
