from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserListCreateView.as_view(), name='user-list-create'),
]