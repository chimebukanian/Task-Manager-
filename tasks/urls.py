from django.urls import path
from . import views

app_name = 'tasks'  # This helps with namespacing

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/tasks/<str:status>/', views.get_tasks, name='get_tasks'),
    path('api/tasks/add', views.add_task, name='add_task'),
    path('api/tasks/update/<int:task_id>/', views.update_task, name='update_task'),
    path('api/tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('api/tasks/search/', views.search_tasks, name='search_tasks'),
]
