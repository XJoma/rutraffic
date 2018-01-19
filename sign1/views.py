from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from sign1.forms import PostForm
from sign1.models import Post1


def sign1(request):
    post = Post1.objects.all().order_by('-id')
    user = auth.get_user(request).username
    context = {}
    context['posts'] = post
    context['username'] = user
    return render(request, 'sign1/sign1.html', context)


def post_single1(request, id):
    post = get_object_or_404(Post1, id=id)
    return render(request, 'sign1/post_single1.html', {'post': post})

def post_new1(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            # post.created = timezone.now()
            form.save()
            return redirect('/')
    return render(request, 'sign1/post_edit1.html', {'form': form})


def post_edit1(request, id):
    post = get_object_or_404(Post1, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created = timezone.now()
            post.save()
            return redirect('sign1/post/%s' % id)
    else:
        form = PostForm(instance=post)
    return render(request, 'sign1/post_edit1.html', {'form': form})


def post_delete1(request, id):
    post = Post1.objects.filter(id=id).delete()
    return redirect('/')
