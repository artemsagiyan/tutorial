from django.shortcuts import render
from rest_framework import generics

from proj.probnik.models import Post
from proj.probnik.serializers import PostSerializer, CommentSerializer


class PostView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
