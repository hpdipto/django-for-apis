from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
	qeuryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	qeuryset = Post.objects.all()
	serializer_class = PostSerializer
