# Study Tasks API

A RESTful Task Management API built with **FastAPI**, **SQLModel**, and **SQLite**, featuring structured backend architecture, data validation, database integration, filtering, pagination, and automated testing.

## Overview

Study Tasks API is a backend application designed to manage study-related tasks through RESTful endpoints. It provides complete task management functionality with persistent database storage, validated request handling, and interactive API documentation.

## Features

- **CRUD Operations:** Create, retrieve, update, and delete tasks.
- **Data Validation:** Validate task data using Pydantic and SQLModel.
- **Database Integration:** Persistent data storage using SQLite.
- **Task Filtering:** Filter tasks by completion status and priority.
- **Search Functionality:** Search tasks by title.
- **Pagination:** Control result sets using offset and limit parameters.
- **Sorting:** Retrieve tasks ordered by priority and task ID.
- **Error Handling:** Handle invalid requests and missing task records using appropriate HTTP status codes.
- **Automated Testing:** Test API functionality using Pytest.
- **Interactive API Documentation:** Automatically generated Swagger UI and ReDoc documentation.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API framework |
| SQLModel | Database models and ORM |
| SQLite | Relational database |
| Pydantic | Data validation |
| SQLAlchemy | Database toolkit |
| Uvicorn | ASGI server |
| Pytest | Automated testing |
| HTTPX | HTTP client for API testing |
| Git & GitHub | Version control |

## Project Structure

```text
study-tasks-api/
│
├── main.py             # API endpoints and application setup
├── models.py           # Database and validation models
├── database.py         # Database engine and session management
├── test_main.py        # Automated API tests
├── requirements.txt    # Project dependencies
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/pratikkunjar/study-tasks-api.git
```

### 2. Navigate to the Project Directory

```bash
cd study-tasks-api
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI automatically generates interactive API documentation.

| Documentation | URL |
|---|---|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Check API health |
| GET | `/version` | Get API version |
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a specific task |
| PATCH | `/tasks/{task_id}` | Update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Filtering, Search and Pagination

The `GET /tasks` endpoint supports query parameters for filtering and pagination.

| Parameter | Description | Example |
|---|---|---|
| `done` | Filter by task completion status | `done=true` |
| `priority` | Filter by priority (1–5) | `priority=3` |
| `search` | Search by task title | `search=python` |
| `offset` | Number of records to skip | `offset=10` |
| `limit` | Maximum records to return (1–100) | `limit=20` |

**Example Request:**

```http
GET /tasks?done=true&priority=3&offset=0&limit=10
```

This request retrieves completed tasks with priority 3, starting from the first record and returning a maximum of 10 results.

## Database Configuration

The application uses SQLite by default and automatically creates the required database tables during application startup.

The database URL can also be configured through the `DATABASE_URL` environment variable, allowing the application to use PostgreSQL when configured appropriately.

## Running Tests

Run the automated test suite using:

```bash
pytest -v
```

## Author

**Prateek Kunjar**

GitHub: [@pratikkunjar](https://github.com/pratikkunjar)

Repository: [Study Tasks API](https://github.com/pratikkunjar/study-tasks-api)
