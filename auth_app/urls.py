from django import urls
from django.urls import path, include
from .views import RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
]