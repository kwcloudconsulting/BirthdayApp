from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from .forms import PostForm

def index(request):
    return render(request, 'index.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
