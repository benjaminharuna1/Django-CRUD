from django.views.generic.edit import CreateView
from .models import Post

class PostLisyView:
    model=Post


class PostCreateView:
    model = Post

class PostCreateView:
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy(“blog:all”)

class PostDetailView:
    model = Post

class PostUpdateView:
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDeleteView:
    model = Post
    fields = "__all__"


