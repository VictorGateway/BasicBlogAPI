from rest_framework import generics, viewsets
from .serializers import PostSerializer, UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class= PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
    permission_classes = (IsAdminUser,)