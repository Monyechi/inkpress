from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Post
import traceback
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .decorators import admin_required
from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required
def drafts(request):
    # Assuming the author should only see their own drafts
    drafts = Post.objects.filter(author=request.user, submitted=False)
    return render(request, 'articles/drafts.html', {'drafts': drafts})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'shared/signup.html', {'form': form})

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title', 'content'] = self.object.title
        return context

def landing_page(request):
    return render(request, 'articles/index.html')

@admin_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.submitted = False  # Always start as a draft
            post.save()
            return redirect('/drafts/')  # Redirect to drafts page
    else:
        form = PostForm()
    return render(request, 'articles/create_post.html', {'form': form})