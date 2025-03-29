from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import PostDetailView, landing_page, create_post, drafts, signup

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='shared/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', signup, name='signup'),
    path('posts/create/', create_post, name='create-post'),
    path('drafts/', drafts, name='drafts'),
]
