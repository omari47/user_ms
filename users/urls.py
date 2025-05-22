from django.urls import path
from .views import RegisterUserView, UserListView, UserDetailView, LogoutView, HomeListView

# Routes are included twice in project urls.py:
# 1. Under /api/ prefix for API endpoints
# 2. At root level for home page access

urlpatterns = [
    # Home page and documentation
    path('', HomeListView.as_view(), name='home'),

    # API endpoints
    path('register/', RegisterUserView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

