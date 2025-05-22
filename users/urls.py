from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, UserListView, UserDetailView, LogoutView

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

