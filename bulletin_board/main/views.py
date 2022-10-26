from django.shortcuts import render
from flask import redirect
from .models import Post
# Create your views here.

# calling index.html page


def index(request):
    return render(request, 'main/index.html')

# calling blog.html page


def blog(request):
    # Saving all the Post in the postlist
    postlist = Post.objects.all()
    # when opening the blog.html page, to get the postlist also
    return render(request, 'main/blog.html', {'postlist': postlist})

# posting


def posting(request, pk):
    # searching for a post with pk(primary_key)
    post = Post.objects.get(pk=pk)
    # when opening the posting.html page, to get the post with the name 'post'
    return render(request, 'main/posting.html', {'post': post})


def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Post.objects.create(
                posttitle=request.POST['posttitle'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article = Post.objects.create(
                posttitle=request.POST['posttitle'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')
