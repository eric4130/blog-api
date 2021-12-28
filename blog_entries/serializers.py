from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user_name', 'slug',
                  'title', 'body', 'created_at')
        model = Post
