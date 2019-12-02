from .models import PostLikeMap
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.forms.models import model_to_dict
import json


@receiver(post_save, sender=PostLikeMap)
def announce_like(sender, instance, created, **kwargs):
    print("working")
    if created:
        channel_layer = get_channel_layer()
        username = instance.user_id.username
        title = instance.post_id.title
        async_to_sync(channel_layer.group_send)(
            "notification", {"type": "liked_notification", "event": "like", "user": username, "title": title, "author": instance.post_id.user_id.id}
        )