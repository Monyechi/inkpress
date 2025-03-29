from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Post
import traceback
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
