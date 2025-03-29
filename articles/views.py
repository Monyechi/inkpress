from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Post
import traceback
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .decorators import admin_required
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required
def drafts(request):
    drafts = Post.objects.filter(author=request.user, submitted=False)
    return render(request, "articles/drafts.html", {"drafts": drafts})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "shared/signup.html", {"form": form})


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title", "content"] = self.object.title
        return context


def landing_page(request):
    return render(request, "articles/index.html")


@admin_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # Check which button was pressed
            action = request.POST.get("action")
            if action == "publish":
                post.submitted = True
            else:  # Default to draft if "Save as Draft" was pressed
                post.submitted = False
            post.save()
            # Redirect based on the action
            if post.submitted:
                # If published, redirect to index page
                return redirect("/")
            else:
                # If saved as draft, redirect to drafts page
                return redirect("/drafts/")
    else:
        form = PostForm()
    return render(request, "articles/create_post.html", {"form": form})


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            error = "Invalid username or password."
            return render(request, "shared/login.html", {"error": error})
    else:
        return render(request, "shared/login.html")


def custom_logout(request):
    logout(request)
    return redirect("/")
