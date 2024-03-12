from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    context = {
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html', context=context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post' : post,
    }
    return render(request, 'blog/post_detail.html', context=context)

