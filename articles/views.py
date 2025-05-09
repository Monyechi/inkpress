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
    try:
        drafts = Post.objects.filter(author=request.user, submitted=False)
        return render(request, "articles/drafts.html", {"drafts": drafts})
    except Exception as e:
        error_message = "An unexpected error occurred while retrieving drafts."
        traceback.print_exc()  # Log the error for debugging purposes
        return render(request, "articles/drafts.html", {"drafts": [], "error": error_message})


def signup(request):
    try:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("/")
        else:
            form = UserCreationForm()
        return render(request, "shared/signup.html", {"form": form})
    except Exception as e:
        error_message = "An unexpected error occurred during signup."
        traceback.print_exc()  # Log the error for debugging purposes
        return render(request, "shared/signup.html", {"form": UserCreationForm(), "error": error_message})


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title", "content"] = self.object.title
        return context


def landing_page(request):
    # Retrieve only published posts
    published_posts = Post.objects.filter(submitted=True)
    return render(request, "articles/index.html", {"posts": published_posts})


@admin_required
def create_post(request):
    try:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                # Use the author provided in the form; if not provided, default to the logged-in user.
                if not post.author:
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
                    return redirect("/")
                else:
                    return redirect("/drafts/")
        else:
            form = PostForm()
            print("request.user:", request.user)
        return render(request, "articles/create_post.html", {"form": form})
    except Exception as e:
        error_message = "An unexpected error occurred while creating the post."
        traceback.print_exc()  # Log the error for debugging purposes
        return render(request, "articles/create_post.html", {"form": PostForm(), "error": error_message})


def custom_login(request):
    try:
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
    except Exception as e:
        error_message = "An unexpected error occurred during login."
        traceback.print_exc()  # Log the error for debugging purposes
        return render(request, "shared/login.html", {"error": error_message})


def custom_logout(request):
    try:
        logout(request)
        return redirect("/")
    except Exception as e:
        error_message = "An unexpected error occurred during logout."
        traceback.print_exc()  # Log the error for debugging purposes
        return HttpResponseServerError(error_message)
