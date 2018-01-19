from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from sign3.forms import PostForm
from sign3.models import Post3


def sign3(request):
    post = Post3.objects.all().order_by('-id')
    user = auth.get_user(request).username
    context = {}
    context['posts'] = post
    context['username'] = user
    return render(request, 'sign3/sign3.html', context)


def post_single3(request, id):
    post = get_object_or_404(Post3, id=id)
    return render(request, 'sign3/post_single3.html', {'post': post})

def post_new3(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            # post.created = timezone.now()
            form.save()
            return redirect('/')
    return render(request, 'sign3/post_edit3.html', {'form': form})


def post_edit3(request, id):
    post = get_object_or_404(Post3, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created = timezone.now()
            post.save()
            return redirect('sign3/post/%s' % id)
    else:
        form = PostForm(instance=post)
    return render(request, 'sign3/post_edit3.html', {'form': form})


def post_delete3(request, id):
    post = Post3.objects.filter(id=id).delete()
    return redirect('/')
