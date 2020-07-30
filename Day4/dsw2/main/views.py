from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'a': postlist})

def detailpost(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/postdetail.html', {'b': post})

def newpost(request):
    if request.method == 'POST':
        if request.POST['c']:
            new_article = Post.objects.create(
                postname=request.POST['a'],
                contents=request.POST['b'],
                mainphoto=request.POST['c']
            )
        else:
            new_article = Post.objects.create(
                postname=request.POST['a'],
                contents=request.POST['b'],
                mainphoto=request.POST['c']
            )
        return redirect('/blog/')
    return render(request, 'main/newpost.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})
