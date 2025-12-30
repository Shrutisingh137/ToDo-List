# ToDo List API Documentation

## Base URL
```
http://127.0.0.1:8000
```

## Authentication
Currently, no authentication is required for API access.

## Endpoints

### 1. Create Task

**Endpoint:** `POST /api/tasks/create/`

**Description:** Creates a new task with the provided data.

**Request Body:**
```json
{
  "title": "Learn Django",
  "description": "Practice building REST APIs",
  "due_date": "2025-01-10",
  "status": "pending"
}
```

**Response (Success - 201 Created):**
```json
{
  "id": 1,
  "message": "Task created successfully"
}
```

**Response (Error - 400 Bad Request):**
```json
{
  "error": "Title is required"
}
```

**Required Fields:**
- `title` (string, max 100 characters)

**Optional Fields:**
- `description` (string)
- `due_date` (string, format: YYYY-MM-DD)
- `status` (string: "pending", "inprogress", "completed" - defaults to "pending")

---

### 2. Get All Tasks

**Endpoint:** `GET /api/tasks/`

**Description:** Retrieves all tasks ordered by creation date (newest first).

**Response (Success - 200 OK):**
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Learn Django",
      "description": "Practice building REST APIs",
      "due_date": "2025-01-10",
      "status": "pending"
    },
    {
      "id": 2,
      "title": "Write Tests",
      "description": "Add comprehensive test coverage",
      "due_date": null,
      "status": "inprogress"
    }
  ]
}
```

---

### 3. Update Task

**Endpoint:** `PUT /api/tasks/<task_id>/`

**Description:** Updates an existing task with the provided data.

**Request Body:**
```json
{
  "title": "Updated Task Title",
  "description": "Updated description",
  "due_date": "2025-01-15",
  "status": "completed"
}
```

**Response (Success - 200 OK):**
```json
{
  "message": "Task updated successfully"
}
```

**Response (Error - 404 Not Found):**
```json
{
  "error": "Task not found"
}
```

**Notes:**
- Only include fields you want to update
- All fields are optional in update requests
- `due_date` can be set to `null` to remove the due date

---

### 4. Delete Task

**Endpoint:** `DELETE /api/tasks/<task_id>/delete/`

**Description:** Deletes the task with the specified ID.

**Response (Success - 200 OK):**
```json
{
  "message": "Task deleted successfully"
}
```

**Response (Error - 404 Not Found):**
```json
{
  "error": "Task not found"
}
```

---

## Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid request data |
| 404 | Not Found - Resource not found |
| 405 | Method Not Allowed - HTTP method not supported |
| 500 | Internal Server Error - Server error |

## Data Types

### Task Object
```json
{
  "id": "integer",
  "title": "string (max 100 chars)",
  "description": "string",
  "due_date": "string (YYYY-MM-DD) or null",
  "status": "string (pending|inprogress|completed)",
  "created_at": "datetime (auto-generated)"
}
```

### Status Values
- `pending` - Task is pending
- `inprogress` - Task is in progress
- `completed` - Task is completed

## Error Handling

All API errors return JSON responses with an `error` field containing a descriptive message.

## Examples

### Using curl

**Create Task:**
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/create/ \
  -H "Content-Type: application/json" \
  -d '{"title": "New Task", "status": "pending"}'
```

**Get Tasks:**
```bash
curl http://127.0.0.1:8000/api/tasks/
```

**Update Task:**
```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

**Delete Task:**
```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/delete/
```

### Using Python (requests library)

```python
import requests

# Create task
response = requests.post('http://127.0.0.1:8000/api/tasks/create/', json={
    'title': 'Learn Python',
    'description': 'Study Python programming',
    'status': 'pending'
})
print(response.json())

# Get all tasks
response = requests.get('http://127.0.0.1:8000/api/tasks/')
tasks = response.json()['tasks']
print(f"Total tasks: {len(tasks)}")
```

## Rate Limiting

Currently, no rate limiting is implemented.

## Versioning

This is version 1.0 of the API. Future versions will include proper versioning in the URL path.