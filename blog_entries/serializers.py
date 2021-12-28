from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user_name', 'title', 'get_image1', 'get_image2', 'get_image3', 'body', 'created_at')
        model = Post
