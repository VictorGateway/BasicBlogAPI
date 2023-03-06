from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    permission_classes= (IsAuthorOrReadOnly,)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes= (IsAuthorOrReadOnly,)