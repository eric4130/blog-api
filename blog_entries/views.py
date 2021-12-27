from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetail(APIView):

    def get_object(self, post_id):
        return Post.objects.get(id=post_id)

    def get(self, request, post_id, format=None):
        post = self.get_object(post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
