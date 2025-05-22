# User Management System

A robust Django-based user management system that provides REST API endpoints for user authentication, registration, and management. Built with Django REST framework and JWT authentication.

## Features

- User registration and authentication
- JWT-based token authentication
- User profile management (CRUD operations)
- API documentation interface
- Secure password handling
- Phone number and address management

## Stack Used
- **Backend**: Django 5.0+, Django REST Framework
- **Authentication**: JWT (JSON Web Tokens) using `djangorestframework-simplejwt`
- **Database**: SQLite (default, configurable for other databases)
- **Documentation**: Built-in API documentation interface

## Setup Instructions

1. **Clone the Repository**:
   ```powershell
   git clone <repository-url>
   cd user_management_system
   ```

2. **Create and Activate Virtual Environment**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**:
   ```powershell
   python manage.py migrate
   ```

5. **Create Admin User**:
   ```powershell
   python manage.py createsuperuser
   ```

6. **Run Development Server**:
   ```powershell
   python manage.py runserver
   ```

7. **Access the Application**:
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - API Documentation: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - API Root: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

## API Endpoints

1. **User Registration**:
   - URL: `/api/register/`
   - Method: `POST`
   - Body:
     ```json
     {
       "username": "testuser",
       "email": "testuser@example.com",
       "password": "password123",
       "phone_number": "1234567890",
       "address": "123 Test Street"
     }
     ```

2. **Authentication (Get Token)**:
   - URL: `/api/token/`
   - Method: `POST`
   - Body:
     ```json
     {
       "username": "testuser",
       "password": "password123"
     }
     ```
   - Response includes both access and refresh tokens

3. **Refresh Token**:
   - URL: `/api/token/refresh/`
   - Method: `POST`
   - Body:
     ```json
     {
       "refresh": "<refresh_token>"
     }
     ```

4. **User Management**:
   - List Users: `GET /api/users/`
   - Get User: `GET /api/users/{id}/`
   - Update User: `PUT /api/users/{id}/`
   - Delete User: `DELETE /api/users/{id}/`
   - All require header: `Authorization: Bearer <access_token>`

5. **Logout**:
   - URL: `/api/logout/`
   - Method: `POST`
   - Requires: `Authorization: Bearer <access_token>`
   - Body:
     ```json
     {
       "refresh": "<refresh_token>"
     }
     ```

## Security Features

- Password hashing using Django's authentication system
- JWT token authentication with refresh capability
- Token blacklisting on logout
- CSRF protection
- Secure password validation

## Development Notes

- Debug mode should be disabled in production
- Environment variables should be properly configured
- Use Postman collection (available at home page) for API testing
- Custom user model includes additional fields for phone and address
- All API endpoints (except registration and token) require authentication

## Error Handling

The API provides clear error messages for:
- Invalid credentials
- Missing required fields
- Authentication failures
- Resource not found
- Permission denied

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
