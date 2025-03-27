from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'articles/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['content'] = self.object.content
        return context

def landing_page(request):
    post = get_object_or_404(Post, pk=1)
    return render(request, 'articles/post_detail.html', {
        'object': post,
        'title': post.title,
        'content': post.content
    })
