from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from sign2.forms import PostForm
from sign2.models import Post2


def sign2(request):
    post = Post2.objects.all().order_by('-id')
    user = auth.get_user(request).username
    context = {}
    context['posts'] = post
    context['username'] = user
    return render(request, 'sign2/sign2.html', context)


def post_single2(request, id):
    post = get_object_or_404(Post2, id=id)
    return render(request, 'sign2/post_single2.html', {'post': post})

def post_new2(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            # post.created = timezone.now()
            form.save()
            return redirect('/')
    return render(request, 'sign2/post_edit2.html', {'form': form})


def post_edit2(request, id):
    post = get_object_or_404(Post2, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created = timezone.now()
            post.save()
            return redirect('sign2/post2/%s' % id)
    else:
        form = PostForm(instance=post)
    return render(request, 'sign2/post_edit2.html', {'form': form})


def post_delete2(request, id):
    post = Post2.objects.filter(id=id).delete()
    return redirect('/')
