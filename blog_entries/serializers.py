from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user_name', 'author', 'slug',
                  'title', 'body', 'created_at', 'updated_at')
        model = Post
