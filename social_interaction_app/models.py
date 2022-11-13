from django.db import models
from social_app.models import *
# Create your models here.


class Post(models.Model):
    post_box = models.TextField()
    liked = models.ManyToManyField(Profile, blank=True, related_name= 'likes')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ('-created_at',)

    def __str__(self):
        return self.post_box[:15]


class Comment(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_box = models.TextField(max_length=200)

LIKE_CHOICES = (

    ('Like',True),
    ('Unlike',False)

)


class Like(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.BooleanField(choices=LIKE_CHOICES)