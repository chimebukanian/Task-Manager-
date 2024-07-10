# Tasky - Task Management Dashboard

## Setup Instructions

1. Clone the repository:https://github.com/chimebukanian/Task-Manager-.git

2. Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install dependencies:pip install -r requirements.txt

4. Apply migrations:python manage.py migrate

5. Create a superuser:python manage.py createsuperuser

6. Run the development server:python manage.py runserver

7. Access the application at `http://localhost:8000`

## Running Tests

To run the unit tests:python manage.py test

## Project Structure

- `taskmanager/`: Main project directory
  - `settings.py`: Project settings
  - `urls.py`: Main URL configuration
- `tasks/`: App directory
  - `models.py`: Task model definition
  - `views.py`: View functions and API endpoints
  - `forms.py`: Form definitions for task creation/editing
  - `tests.py`: Unit tests
  - `templates/`: HTML templates
    - `dashboard.html`: Main dashboard template
  - `static/`: Static files (CSS, JS)

## Features

- User authentication
- CRUD operations for tasks
- Drag-and-drop functionality for changing task status
- Search, filter, and sort tasks
- Responsive design

## Technologies Used

- Backend: Django
- Frontend: HTML, TailwindCSS, jQuery
- Database: SQLite (default), can be changed to PostgreSQL for production

## API Endpoints

- `GET /api/tasks/<status>/`: Get tasks by status
- `POST /api/tasks/add/`: Add a new task
- `PUT /api/tasks/update/<task_id>/`: Update an existing task
- `DELETE /api/tasks/delete/<task_id>/`: Delete a task
- `GET /api/tasks/search/?q=<query>`: Search tasks
