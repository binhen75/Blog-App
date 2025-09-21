from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

@login_required
def index(request):
    posts = BlogPost.objects.order_by('date_added') 
    context = {'posts' : posts}
    if request.method == 'POST':
        return redirect('blogs:new_post')
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)   

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)

def check_topic_owner(owner, user):
    if owner != user:
        raise Http404
