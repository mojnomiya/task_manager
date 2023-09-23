```markdown
# Task Manager

A brief project description goes here.

## Table of Contents

- [Set Up and Run the Project](#set-up-and-run-the-project)
- [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)

## Set Up and Run the Project

1. Clone this repository:

   ```
   git clone https://github.com/mojnomiya/task_manager.git
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```
   python manage.py migrate
   ```

6. Run the development server:

   ```
   python manage.py runserver
   ```

The project should now be running at [http://localhost:8000](http://localhost:8000).

## Environment Variables

To set up environment variables for this project, create a `.env` file in the project's root directory and add the following variables:

- `SECRET_KEY`: Your Django secret key.
- `DEBUG`: Set to `True` for development and `False` for production.
- `DB_NAME`: The name of your database.
- `DB_USER`: The username of your database.
- `DB_PASSWORD`: The password of your database.

Example `.env` file:

```
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME= "task_manager"
DB_PASSWORD= "your_password"
```

## API Documentation

### List Tasks

**Endpoint:** `/api/tasks/`

**Method:** `GET`

**Description:** Get a list of tasks.

**Authentication:** Requires user authentication.

**Parameters:**
- `q` (optional): Search query for task titles.
- `priority` (optional): Filter tasks by priority (e.g., 'High', 'Medium', 'Low').
- `due_date` (optional): Filter tasks by due date (e.g., '2023-09-30').
- `is_complete` (optional): Filter tasks by completion status (e.g., 'True' or 'False').

**Response:**
- Status Code: 200 OK
- Body: JSON array of task objects.

### Create Task

**Endpoint:** `/api/tasks/`

**Method:** `POST`

**Description:** Create a new task.

**Authentication:** Requires user authentication.

**Request Body:** JSON object with task details.

**Response:**
- Status Code: 201 Created
- Body: JSON object of the created task.

### Retrieve, Update, Delete Task

**Endpoint:** `/api/tasks/<int:pk>/`

**Methods:** `GET`, `PUT`, `PATCH`, `DELETE`

**Description:** Retrieve, update, or delete a specific task by ID.

**Authentication:** Requires user authentication.

**Response (GET):**
- Status Code: 200 OK
- Body: JSON object of the task.

**Response (PUT, PATCH):**
- Status Code: 200 OK
- Body: JSON object of the updated task.

**Response (DELETE):**
- Status Code: 204 No Content (Task deleted).
```