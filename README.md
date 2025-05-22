# User Management System

This project is a simple user management system built with Django. It allows for creating, updating, deleting, and managing user accounts, as well as token-based authentication for secure access.

## Project Purpose
The purpose of this project is to provide a basic user management system with CRUD operations and authentication APIs. It is designed to demonstrate the use of Django and Django REST Framework for building web applications.

## Stack Used
- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (JSON Web Tokens) using `djangorestframework-simplejwt`
- **Database**: SQLite (default, can be configured for other databases)
- **Frontend**: Django Admin Panel (for management)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd django-template
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - API Endpoints: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

## API Endpoints

1. **Register a User**:
   - URL: `/api/register/`
   - Method: `POST`
   - Body (JSON):
     ```json
     {
       "username": "testuser",
       "email": "testuser@example.com",
       "password": "password123"
     }
     ```

2. **Obtain Token**:
   - URL: `/api/token/`
   - Method: `POST`
   - Body (JSON):
     ```json
     {
       "username": "testuser",
       "password": "password123"
     }
     ```

3. **Refresh Token**:
   - URL: `/api/token/refresh/`
   - Method: `POST`
   - Body (JSON):
     ```json
     {
       "refresh": "<refresh_token>"
     }
     ```

4. **List Users**:
   - URL: `/api/users/`
   - Method: `GET`
   - Headers: `Authorization: Bearer <access_token>`

5. **Retrieve, Update, or Delete a User**:
   - URL: `/api/users/<user_id>/`
   - Methods: `GET`, `PUT`, `DELETE`
   - Headers: `Authorization: Bearer <access_token>`

6. **Logout**:
   - URL: `/api/logout/`
   - Method: `POST`
   - Body (JSON):
     ```json
     {
       "refresh": "<refresh_token>"
     }
     ```

## Notes
- Ensure you configure any required environment variables in a `.env` file.
- Use Postman or any API client to test the endpoints and collect JSON responses.
