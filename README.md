# Todo API

This project is a simple **Todo API** built using Flask and SQLAlchemy. It allows users to manage tasks with features like creating, updating, deleting, and filtering tasks. The project is containerized using Docker for easy deployment.

---

## Project Structure

```
todo-api/
├── app.py               # Main application file
├── models.py            # Database models
├── Dockerfile           # Dockerfile for building the API container
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies
├── .dockerignore        # Files to ignore in the Docker build
└── README.md            # Project documentation
```

---

## Files Overview

### 1. `app.py`
This is the main application file that defines the Flask API. It includes the following endpoints:

- **`GET /tasks`**: Retrieve all tasks with optional filters (`completed`, `due_date`, `priority`).
- **`POST /tasks`**: Create a new task.
- **`GET /tasks/<id>`**: Retrieve a specific task by ID.
- **`PUT /tasks/<id>`**: Update a task by ID.
- **`DELETE /tasks/<id>`**: Delete a task by ID.
- **`PUT /tasks/<id>/complete`**: Mark a task as completed.
- **`PUT /tasks/<id>/incomplete`**: Mark a task as incomplete.
- **`PUT /tasks/<id>/priority`**: Update the priority of a task.

### 2. `models.py`
Defines the database model for the `Task` entity using SQLAlchemy. The `Task` model includes:
- `id`: Primary key.
- `title`: Title of the task (required).
- `description`: Optional description of the task.
- `due_date`: Due date in `YYYY-MM-DD` format.
- `completed`: Boolean indicating if the task is completed (default: `False`).
- `priority`: Priority level (`low`, `medium`, `high`; default: `medium`).

### 3. `Dockerfile`
Defines the Docker image for the application:
- Uses the latest Python image.
- Installs dependencies from `requirements.txt`.
- Copies the application code into the container.
- Exposes port `5000` for the Flask app.
- Runs the app using `python app.py`.

### 4. `docker-compose.yml`
Defines the multi-container setup for the project:
- **`todo-api`**: The Flask application container.
- **`db`**: A SQLite container for persistent storage.
- Uses a volume (`db_data`) to persist the database file.

### 5. `.dockerignore`
Specifies files and directories to exclude from the Docker build context:
- Python cache files (`__pycache__`, `*.pyc`, etc.).
- SQLite database files (`*.db`, `*.sqlite3`).
- Environment files (`.env`).

---

## How to Run the Project

### Prerequisites
- Docker and Docker Compose installed on your system.

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/ElDEEB21/todo-api
    cd todo-api
    ```

2. Build and start the containers:
    ```bash
    docker-compose up --build
    ```

3. Access the API at `http://localhost:5000`.

---

## API Usage

### Example Task Object
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "due_date": "2023-12-01",
  "completed": false,
  "priority": "high"
}
```

### Example Requests
- **Create a Task**:
  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, Bread, Eggs", "due_date": "2023-12-01", "priority": "high"}' \
  http://localhost:5000/tasks
  ```

- **Get All Tasks**:
  ```bash
  curl http://localhost:5000/tasks
  ```

- **Update a Task**:
  ```bash
  curl -X PUT -H "Content-Type: application/json" \
  -d '{"completed": true}' \
  http://localhost:5000/tasks/1
  ```

- **Delete a Task**:
  ```bash
  curl -X DELETE http://localhost:5000/tasks/1
  ```

---

## Notes
- The database is stored in a SQLite file (`database.db`) inside the `db` container.
- The API is designed to be lightweight and easy to extend.

