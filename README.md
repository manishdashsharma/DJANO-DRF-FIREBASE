# Django + Django RestFramework + Firebase Setup

This repository provides a comprehensive setup guide for creating a Django project using Django Rest Framework and integrating Firebase. It covers the initial project setup, configuration steps, and creating your first API endpoint.

### Features:

- **Initial Setup**: Detailed steps to create a new Django project and application.
- **Configuration**: Instructions for configuring `settings.py`, `urls.py`, and middleware settings.
- **Health Check Endpoint**: A basic health check endpoint to confirm the server's status.
- **First API Endpoint**: A guide to create an API endpoint that returns a welcome message.

### Technologies Used:

- Django
- Django Rest Framework
- Firebase

### Getting Started:

Follow the setup guide in the README to initialize your Django project, configure the settings, and create your first API endpoint.


Clone this repository and start building your Django project with Django Rest Framework and Firebase integration today! 🚀

## Prerequisites

Ensure you have the following installed:

- Python
- pip

## Setup Steps

### 1. Create a New Folder

```bash
mkdir <your_folder_name>
```

### 2. Create a Virtual Environment

#### For macOS:

```bash
python3 -m venv env
```

#### For Windows:

```bash
python -m venv env
```

### 3. Activate the Virtual Environment

#### For macOS:

```bash
source ./env/bin/activate
```

#### For Windows:

```bash
source ./env/Scripts/activate
```

**Note**: Replace `env` with the name you choose for your virtual environment.

### 4. Install Dependencies

```bash
pip install djangorestframework django-cors-headers requests
```

### 5. Create a Django Project

```bash
django-admin startproject core .
```

### 6. Create a Django Application

```bash
python manage.py startapp app
```

## Configuration

### Update `core/settings.py`

- Modify `ALLOWED_HOSTS`:

```python
ALLOWED_HOSTS = ["*"]
```

- Add apps to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'app',
    'rest_framework',
    'corsheaders',
    # ...
]
```

- Update `MIDDLEWARE`:

```python
MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]
```

- Add CORS setting:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

### Update `core/urls.py`

- Import `include`:

```python
from django.urls import path, include
```

- Add a URL pattern for the Django application:

```python
urlpatterns = [
    # ...
    path('api/v1/', include('app.urls')),
    # ...
]
```

### Create `urls.py` for `app`

```bash
touch app/urls.py
```

Add the following code to `app/urls.py`:

```python
from django.urls import path

urlpatterns = []
```

### Create Health Check Endpoint

1. Create `healthcheck.py`:

```bash
touch healthcheck.py
```

2. Add the following code to `healthcheck.py`:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class healthCheck(APIView):
    def get(self, request):
        return Response("If you are seeing this, then the server is up!", status=status.HTTP_200_OK)
```

3. Update `core/urls.py` to include the health check endpoint:

```python
from healthcheck import *

urlpatterns = [
    # ...
    path('', healthCheck.as_view()),
    # ...
]
```

## Starting the Server

Run the following command:

**For macOS**

```bash
python3 manage.py runserver
```

**For Windows**

```bash
python manage.py runserver
```

**Note**: You may see a message about pending migrations; we'll address this shortly.

Visit `http://127.0.0.1:8000/` in your browser. You should see the health check message confirming that the server is running.

## Creating Your First API

### Problem Statement

Create an endpoint with a `GET` method that returns the message: "Welcome to our API service."

1. Update `app/views.py`:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class serviceInfo(APIView):
    def get(self, request):
        return Response({
            "success": True,
            "message": "Welcome to our API service."
        }, status=status.HTTP_200_OK)
```

2. Update `app/urls.py`:

```python
from .views import *

urlpatterns = [
    path('', serviceInfo.as_view())
]
```

### Accessing the API

If the server is not running, start it with `python3 manage.py runserver` (macOS) or `python manage.py runserver` (Windows).

Visit `http://127.0.0.1:8000/api/v1/` in your browser or API client. You should see the following response:

```json
{
    "success": true,
    "message": "Welcome to our API service."
}
```

Congratulations! You have successfully created your first API service using Django 🚀.