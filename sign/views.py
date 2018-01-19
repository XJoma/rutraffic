from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from sign.forms import PostForm
from sign.models import Post


def sign(request):
    post = Post.objects.all().order_by('-id')
    user = auth.get_user(request).username
    context = {}
    context['posts'] = post
    context['username'] = user
    return render(request, 'sign/sign.html', context)


def post_single(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'sign/post_single.html', {'post': post})

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            # post.created = timezone.now()
            form.save()
            return redirect('/')
    return render(request, 'sign/post_edit.html', {'form': form})


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created = timezone.now()
            post.save()
            return redirect('sign/post/%s' % id)
    else:
        form = PostForm(instance=post)
    return render(request, 'sign/post_edit.html', {'form': form})


def post_delete(request, id):
    post = Post.objects.filter(id=id).delete()
    return redirect('/')
