from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('users/', views.CustomUserListView.as_view()),
    path('users/<int:pk>', views.CustomUserDetailView.as_view()),
]