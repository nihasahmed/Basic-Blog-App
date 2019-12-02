from django.shortcuts import render, redirect
from .models import Post, InappPosts, PostLikeMap
from .form import BlogPost
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
from requests import get

# Create your views here.


def index(request):

    userid = 0
    inapp = InappPosts.objects.all()
    if request.method == 'POST':
        pid = request.POST.get('id')
        post = Post.objects.get(pk=pid)
        post.approved = not post.approved
        post.save()
    if request.user.is_authenticated:
        logged = True
        userid = request.user.id
        if not request.user.is_superuser:
            userContent = Post.objects.filter(user_id=request.user.id)
            otherContent = Post.objects.filter(approved=True)
            content = userContent.union(otherContent)
            superu = False
        else:
            content = Post.objects.all()
            superu = True
    else:
        logged = False
        content = Post.objects.filter(approved=True)
        superu = False
    return render(request, 'blog/index.html', {'content': content, 'logged': logged, 'super': superu, 'id': userid, 'inapp': inapp})

@login_required(redirect_field_name='next',login_url='/user/login/')
def createPost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user
            obj.save()
            return redirect('indexpage')
        else:
            print(form.errors)
    return render(request, 'blog/createpost.html', {})


def postView(request, ids):
    user = request.user
    content = Post.objects.get(pk=ids)
    if request.method == 'POST':
        action = request.POST.get('value')
        if action == 'like':
            obj,created = PostLikeMap.objects.get_or_create(user_id=user, post_id=content)
            obj.save()
        else:
            try:
                PostLikeMap.objects.get(user_id=user, post_id=content).delete()
            except PostLikeMap.DoesNotExist:
                pass
    if request.user.is_authenticated:
        logged = True
        try:
            liked = PostLikeMap.objects.get(user_id=user, post_id=content)
            userliked = True
        except PostLikeMap.DoesNotExist:
            userliked = False
    else:
        logged = False
        userliked = False

    return render(request, 'blog/post.html', {'content': content, 'logged': logged, 'liked': userliked})


@login_required(redirect_field_name='next', login_url='/user/login/')
def postEdit(request, ids):
    content = Post.objects.get(pk=ids)
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES, instance=content)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user
            obj.save()
        else:
            print(form.errors)
        return redirect('indexpage')

    if request.user.is_authenticated:
        logged = True
    else:
        logged = False
    return render(request, 'blog/createpost.html', {'content': content, 'logged': logged})


