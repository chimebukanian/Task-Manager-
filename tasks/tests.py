from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from django.urls import reverse
from django.utils import timezone

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        Task.objects.create(
            title='Test Task',
            description='This is a test task',
            status='IN_PROGRESS',
            priority='MEDIUM',
            due_date=timezone.now() + timezone.timedelta(days=1),
            category='Test',
            assigned_to=self.user
        )

    def test_task_creation(self):
        task = Task.objects.get(title='Test Task')
        self.assertEqual(task.description, 'This is a test task')
        self.assertEqual(task.status, 'IN_PROGRESS')
        self.assertEqual(task.assigned_to, self.user)

class TaskViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            status='IN_PROGRESS',
            priority='MEDIUM',
            due_date=timezone.now() + timezone.timedelta(days=1),
            category='Test',
            assigned_to=self.user
        )

    def test_dashboard_view(self):
        response = self.client.get(reverse('tasks:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/dashboard.html')

    def test_get_tasks_api(self):
        response = self.client.get(reverse('tasks:get_tasks', args=['IN_PROGRESS']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_add_task_api(self):
        new_task = {
            'title': 'New Task',
            'description': 'This is a new task',
            'status': 'IN_PROGRESS',
            'priority': 'HIGH',
            'due_date': (timezone.now() + timezone.timedelta(days=2)).isoformat(),
            'category': 'New'
        }
        response = self.client.post(reverse('tasks:add_task'), data=new_task, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_update_task_api(self):
        updated_data = {
            'title': 'Updated Task',
            'description': 'This task has been updated',
            'status': 'COMPLETED',
            'priority': 'LOW',
            'due_date': (timezone.now() + timezone.timedelta(days=3)).isoformat(),
            'category': 'Updated'
        }
        response = self.client.put(
            reverse('tasks:update_task', args=[self.task.id]),
            data=updated_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.title, 'Updated Task')
        self.assertEqual(updated_task.status, 'COMPLETED')

    def test_delete_task_api(self):
        response = self.client.delete(reverse('tasks:delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_search_tasks_api(self):
        response = self.client.get(reverse('tasks:search_tasks') + '?q=Test')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
