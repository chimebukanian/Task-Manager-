from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.urls import reverse
from .models import Task
from .forms import TaskForm
import json

@login_required
def dashboard(request):
    return render(request, 'tasks/dashboard.html')

@login_required
@require_http_methods(["GET"])
def get_tasks(request, status):
    tasks = Task.objects.filter(status=status, assigned_to=request.user).values()
    return JsonResponse(list(tasks), safe=False)

@login_required
@csrf_exempt
@require_POST
def add_task(request):
    data = json.loads(request.body)
    print(data)  # Print received JSON data
    form = TaskForm(data)
    if form.is_valid():
        task = form.save(commit=False)
        task.assigned_to = request.user
        task.save()
        return JsonResponse({'id': task.id, "success": True, "message": "Task added successfully."})
    return JsonResponse({"success": False, "errors": form.errors}, status=400)


@login_required
@csrf_exempt
@require_http_methods(["PUT"])
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_to=request.user)
    data = json.loads(request.body)
    form = TaskForm(data, instance=task)
    if form.is_valid():
        updated_task = form.save()
        return JsonResponse({'message': 'Task updated successfully'})
    return JsonResponse({'error': form.errors}, status=400)

@login_required
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_to=request.user)
    task.delete()
    return JsonResponse({'message': 'Task deleted successfully'})

@login_required
@require_http_methods(["GET"])
def search_tasks(request):
    print('called')
    query = request.GET.get('q', '')
    if query:
        tasks = Task.objects.filter(title__icontains=query, assigned_to=request.user).values()
        print(tasks)
    else:
        tasks = Task.objects.none()  # Or return all tasks if that's the intended behavior
        print(None)
    return JsonResponse(list(tasks), safe=False)
