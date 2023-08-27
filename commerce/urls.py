from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>', views.ProductDetailView.as_view()),
    path('add-product/', views.AddProductView.as_view()),
    path('users/', views.CustomUserListView.as_view()),
    path('users/<int:pk>', views.CustomUserDetailView.as_view()),
]