from django.urls import re_path
from blog.consumers import Notification
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/notification/$', Notification),
]