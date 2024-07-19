from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'due_date', 'assigned_to', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'assigned_to')
    search_fields = ('title', 'description', 'category')

admin.site.register(Task, TaskAdmin)