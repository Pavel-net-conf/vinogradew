from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

class BlogCreatePost(CreateView):

    model = Post

    template_name = 'blog/new_post.html'

    fields = ['author','title','content']


class HomeBlogPage(ListView):
    model = Post
    template_name = 'blog/home_blog.html'
    context_object_name = 'post'

class BlogDetailView(DetailView):
    model = Post

    template_name = 'blog/detail_blog.html'

    context_object_name = 'post'