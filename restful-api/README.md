# RESTful API

## Description

This project explores the fundamentals of RESTful APIs, from basic HTTP concepts to building and securing APIs with Python. It covers consuming APIs from the command line and with Python, developing simple servers, and implementing authentication mechanisms.

## Learning Objectives

- Understand the differences between HTTP and HTTPS
- Consume APIs using curl from the command line
- Use Python's requests library to fetch and process API data
- Build a basic HTTP server with Python's built-in http.server module
- Develop a RESTful API using Flask
- Secure an API with Basic Authentication and JWT tokens

## Requirements

- Python 3.9
- pip packages: requests, Flask, Flask-HTTPAuth, Flask-JWT-Extended, werkzeug

## Installation

```bash
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended
```

## Tasks

### Task 0: Basics of HTTP/HTTPS

Conceptual understanding of the HTTP protocol and its secure variant HTTPS.

Key differences between HTTP and HTTPS:
- HTTP transmits data in plain text; HTTPS encrypts data using SSL/TLS
- HTTPS protects against eavesdropping and data tampering
- HTTPS requires a certificate from a trusted authority

Common HTTP methods:

| Method | Description | Use case |
|--------|-------------|----------|
| GET | Retrieves data | Fetching a web page or API resource |
| POST | Sends data to create a resource | Submitting a form or creating a user |
| PUT | Updates an existing resource | Replacing a user profile |
| DELETE | Removes a resource | Deleting a record |

Common HTTP status codes:

| Code | Name | Description |
|------|------|-------------|
| 200 | OK | Request succeeded |
| 201 | Created | Resource successfully created |
| 301 | Moved Permanently | Resource has a new URL |
| 404 | Not Found | Resource does not exist |
| 500 | Internal Server Error | Server encountered an error |

### Task 1: Consume data from an API using curl

Using curl to interact with the JSONPlaceholder API from the command line.

```bash
# Fetch all posts
curl https://jsonplaceholder.typicode.com/posts

# Fetch only response headers
curl -I https://jsonplaceholder.typicode.com/posts

# Send a POST request
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### Task 2: Consuming and processing data from an API using Python

**File:** task_02_requests.py

Two functions that interact with the JSONPlaceholder API:

- `fetch_and_print_posts()`: fetches all posts, prints the status code and each post title
- `fetch_and_save_posts()`: fetches all posts and saves them to posts.csv with columns id, title, and body

Usage:
```bash
python3 task_02_requests.py
```

### Task 3: Simple API using http.server

**File:** task_03_http_server.py

A basic HTTP server built with Python's standard library, no third-party frameworks.

Endpoints:

| Route | Response |
|-------|----------|
| / | Hello, this is a simple API! |
| /data | JSON object with sample user data |
| /status | OK |
| /info | JSON object with API version info |
| any other | 404 Endpoint not found |

Usage:
```bash
python3 task_03_http_server.py
```

### Task 4: Simple API using Flask

**File:** task_04_flask.py

A RESTful API built with Flask, storing users in memory.

Endpoints:

| Method | Route | Description |
|--------|-------|-------------|
| GET | / | Welcome message |
| GET | /data | List of all usernames |
| GET | /status | Returns OK |
| GET | /users/username | Full user object |
| POST | /add_user | Add a new user |

Usage:
```bash
flask --app task_04_flask.py run
```

Example POST request:
```bash
curl -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "name": "Alice", "age": 25, "city": "San Francisco"}'
```

### Task 5: API Security and Authentication

**File:** task_05_basic_security.py

A Flask API with two layers of authentication: Basic Auth and JWT tokens.

Endpoints:

| Method | Route | Auth | Description |
|--------|-------|------|-------------|
| GET | /basic-protected | Basic Auth | Returns access granted message |
| POST | /login | None | Returns a JWT token |
| GET | /jwt-protected | JWT | Returns access granted message |
| GET | /admin-only | JWT + admin role | Returns admin access message |

Built-in users:

| Username | Password | Role |
|----------|----------|------|
| user1 | password | user |
| admin1 | password | admin |

Usage:
```bash
flask --app task_05_basic_security.py run
```

Example workflow:
```bash
# Basic auth
curl -u user1:password http://localhost:5000/basic-protected

# Get a JWT token
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "password"}'

# Use the token
curl -H "Authorization: Bearer <token>" http://localhost:5000/jwt-protected

# Admin route
curl -H "Authorization: Bearer <admin_token>" http://localhost:5000/admin-only
```

## Repository

- GitHub: holbertonschool-higher_level_programming
- Directory: restful-api
