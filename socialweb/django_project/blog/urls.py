from django.urls import path
from .views import PostListViews, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListViews
from . import views

urlpatterns = [

    path("", PostListViews.as_view(), name="blog-home"),
    path("user/<str:username>", UserPostListViews.as_view(), name="user-posts"),
    path("about/", views.about, name="blog-about"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="blog-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete")
]

