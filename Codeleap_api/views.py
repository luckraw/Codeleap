from django.shortcuts import render
from rest_framework import generics
from Codeleap_api.models import Post
from Codeleap_api.serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



