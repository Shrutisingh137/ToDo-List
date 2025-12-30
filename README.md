# ToDo List App

A Django-based task manager I built to practice full-stack development. Includes both a web interface and REST API.

## What it does

This app lets you manage tasks with:
- Basic CRUD operations (Create, Read, Update, Delete)
- Task status tracking (pending → in progress → completed)
- Due dates and descriptions
- A clean web UI with pagination
- JSON API for external integrations

## Tech Stack

- **Django 6.0** - Backend framework
- **SQLite** - Database (easy for development)
- **HTML/CSS** - Frontend (kept it simple, no JS frameworks)
- **pytest** - Testing

## Quick Start

1. **Set up virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install django pytest pytest-django
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the server:**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to see the app.

## API Usage

The API is pretty straightforward. Here are the main endpoints:

**Create a task:**
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/create/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Django", "status": "pending"}'
```

**Get all tasks:**
```bash
curl http://127.0.0.1:8000/api/tasks/
```

**Update a task:**
```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

**Delete a task:**
```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/delete/
```

Check `API_DOCUMENTATION.md` for full details.

## Project Structure

```
todo_project/
├── tasks/                    # Main app
│   ├── models.py            # Task model
│   ├── views_api.py         # API endpoints
│   ├── views_web.py         # Web pages
│   ├── urls.py              # URL routing
│   ├── templates/tasks/     # HTML templates
│   └── tests/               # API tests
├── todo_project/            # Django project settings
├── db.sqlite3               # Database
└── manage.py               # Django CLI
```

## Running Tests

```bash
pytest
```

I wrote tests for all the API endpoints to make sure they work correctly.

## What I Learned

Building this helped me understand:
- Django's MTV pattern
- REST API design
- Database relationships
- Testing Django apps
- Basic HTML/CSS for web interfaces

## Future Ideas

If I were to expand this:
- Add user authentication
- Task categories/tags
- Email notifications for due dates
- Better mobile responsiveness
- Search and filtering

## Notes

- No authentication yet (would add that for production)
- Uses SQLite for simplicity
- API returns JSON, web interface uses Django templates
- Pagination on the web view to handle lots of tasks