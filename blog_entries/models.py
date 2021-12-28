from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_image1(self):
        if self.image1:
            return 'http://127.0.0.1:8000' + self.image1.url
        return ''
    def get_image2(self):
        if self.image2:
            return 'http://127.0.0.1:8000' + self.image2.url
        return ''
    def get_image3(self):
        if self.image3:
            return 'http://127.0.0.1:8000' + self.image3.url
        return ''
    
