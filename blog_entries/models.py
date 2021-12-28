from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'
