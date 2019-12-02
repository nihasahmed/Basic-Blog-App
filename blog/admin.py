from django.contrib import admin
from .models import Post, InappPosts, PostLikeMap
# Register your models here.
admin.site.register(Post)
admin.site.register(InappPosts)
admin.site.register(PostLikeMap)

