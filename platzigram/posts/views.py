#Django
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Form
from posts.forms import PostForm
# Models
from posts.models import Post


# Create your views here.
@login_required
def list_posts(requests):
    """
        The def render takes 3 parameter, the request, the HTML and the context
    """
    posts = Post.objects.all().order_by('-created')
    return render(requests, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    """Def to create new posts views"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request=request, template_name='posts/new.html', context={'form': form, 'user': request.user, 'profile': request.user.profile})

