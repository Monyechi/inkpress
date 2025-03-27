from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Post
import traceback
from django.http import HttpResponseServerError

class PostDetailView(DetailView):
    model = Post
    template_name = 'articles/post_detail.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['title'] = self.object.title
            context['content'] = self.object.content
            return context
        except Exception as e:
            traceback.print_exc()
            return HttpResponseServerError("An error occurred while processing the request.")

def landing_page(request):
    post = Post.objects.first()  
    if not post:
        return render(request, 'articles/post_detail.html', {
            'object': None,
            'title': 'No Post Available',
            'content': 'There is no post to display yet.'
        })

    return render(request, 'articles/post_detail.html', {
        'object': post,
        'title': post.title,
        'content': post.content
    })
