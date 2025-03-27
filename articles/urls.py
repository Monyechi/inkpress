from django.urls import path
from .views import PostDetailView, landing_page

urlpatterns = [
    path('', landing_page, name='landing-page'),  # Landing page at /
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
