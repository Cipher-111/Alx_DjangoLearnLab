from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    login_view, logout_view, register_view, profile_view
)

urlpatterns = [

    # Authentication
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),

    # Blog CRUD
    path("", PostListView.as_view(), name="home"), 
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
