from django.shortcuts import render

from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics


from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework import status
# Create your views here.``

class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RegisterAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer

    def post(self, request):
        data = {
            'username': request.data.get('username'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'user_type': request.data.get('user_type'),
            'password': request.data.get('password'),
            'password2': request.data.get('password2'),

        }

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
