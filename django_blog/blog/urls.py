from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    register_view, login_view, logout_view, profile_view
)

urlpatterns = [
    # Authentication
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),

    # CRUD URLs exactly as ALX expects
    path("", PostListView.as_view(), name="home"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
