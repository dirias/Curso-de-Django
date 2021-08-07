#Django
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Form
from posts.forms import PostForm
# Models
from posts.models import Post


# Create your views here.
class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 25
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """return post detail."""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    """Class based view to create posts."""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

""" code replaced by PostCreateView
@login_required
def create_post(request):
    "Def to create new posts views
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    return render(request=request, template_name='posts/new.html', context={'form': form, 'user': request.user, 'profile': request.user.profile})

"""