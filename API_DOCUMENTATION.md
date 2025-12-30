```md
Base URL:
http://127.0.0.1:8000

yaml
Copy code

---

## 1. Create Task API

**POST** `/api/tasks/create/`

### Request Body
```json
{
  "title": "Learn Django",
  "description": "Practice APIs",
  "due_date": "2025-01-10",
  "status": "pending"
}
Success Response
json
Copy code
{
  "id": 1,
  "message": "Task created successfully"
}
2. Get All Tasks API
GET /api/tasks/

Response
json
Copy code
{
  "tasks": [
    {
      "id": 1,
      "title": "Learn Django",
      "description": "Practice APIs",
      "due_date": "2025-01-10",
      "status": "pending"
    }
  ]
}
3. Update Task API
PUT /api/tasks/<task_id>/

Request Body
json
Copy code
{
  "title": "Updated Task",
  "status": "completed"
}
Response
json
Copy code
{
  "message": "Task updated successfully"
}
4. Delete Task API
DELETE /api/tasks/<task_id>/delete/

Response
json
Copy code
{
  "message": "Task deleted successfully"
}
Status Codes
Code	Meaning
200	OK
201	Created
400	Bad Request
404	Not Found
500	Server Error

yaml
Copy code

---

# 🟢 FINAL CHECK (DO THIS ONCE)

Run:
```powershell
dir