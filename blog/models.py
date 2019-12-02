from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pic = models.ImageField(null=True, blank=True)
    content = models.TextField()
    postdate = models.DateTimeField(auto_now=False, auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True, auto_now_add=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


class PostLikeMap(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    likedon = models.DateTimeField(auto_now=False, auto_now_add=True)


class InappPosts(models.Model):
    title = models.TextField()
    link = models.TextField()
    date_added =  models.DateTimeField(auto_now=False, auto_now_add=True)


