import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task

logger = logging.getLogger(__name__)


@csrf_exempt
def create_task(request):
    """
    API to create a new task
    Method: POST
    """
    if request.method != 'POST':
        return JsonResponse(
            {'error': 'Method not allowed'},
            status=405
        )

    try:
        data = json.loads(request.body)

        title = data.get('title')
        if not title:
            return JsonResponse(
                {'error': 'Title is required'},
                status=400
            )

        task = Task.objects.create(
            title=title,
            description=data.get('description', ''),
            due_date=data.get('due_date'),
            status=data.get('status', 'pending')
        )

        return JsonResponse(
            {
                'id': task.id,
                'message': 'Task created successfully'
            },
            status=201
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {'error': 'Invalid JSON'},
            status=400
        )

    except Exception as e:
        logger.error(f"Create Task API Error: {str(e)}")
        return JsonResponse(
            {'error': 'Internal server error'},
            status=500
        )


def get_tasks(request):
    """
    API to fetch all tasks
    Method: GET
    """
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'Method not allowed'},
            status=405
        )

    tasks = Task.objects.all().order_by('-created_at')

    result = []
    for task in tasks:
        result.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date,
            'status': task.status
        })

    return JsonResponse({'tasks': result}, status=200)


@csrf_exempt
def update_task(request, task_id):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        data = json.loads(request.body)
        task = Task.objects.get(id=task_id)

        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        task.due_date = data.get('due_date') or None
        task.save()

        return JsonResponse({'message': 'Task updated successfully'})

    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)


@csrf_exempt
def delete_task(request, task_id):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'})

    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

