from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from sign4.forms import PostForm
from sign4.models import Post4


def sign4(request):
    post = Post4.objects.all().order_by('-id')
    user = auth.get_user(request).username
    context = {}
    context['posts'] = post
    context['username'] = user
    return render(request, 'sign4/sign4.html', context)


def post_single4(request, id):
    post = get_object_or_404(Post4, id=id)
    return render(request, 'sign4/post_single4.html', {'post': post})

def post_new4(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            # post.created = timezone.now()
            form.save()
            return redirect('/')
    return render(request, 'sign4/post_edit4.html', {'form': form})


def post_edit4(request, id):
    post = get_object_or_404(Post4, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created = timezone.now()
            post.save()
            return redirect('sign4/post/%s' % id)
    else:
        form = PostForm(instance=post)
    return render(request, 'sign4/post_edit4.html', {'form': form})


def post_delete4(request, id):
    post = Post4.objects.filter(id=id).delete()
    return redirect('/')
