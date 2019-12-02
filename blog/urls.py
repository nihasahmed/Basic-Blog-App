
from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.index, name='indexpage'),
    path('create/', views.createPost, name='createpost'),
    path('user/', include('logincontrol.urls')),
    path('posts/<ids>', views.postView, name='posts'),
    path('edit/<ids>', views.postEdit, name='edit'),
]
