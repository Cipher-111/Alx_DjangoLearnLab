from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post
from .forms import RegisterForm, PostForm


# ============================
# Authentication Views
# ============================

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "blog/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        request.user.email = email
        request.user.save()
        messages.success(request, "Profile updated successfully")

    return render(request, "blog/profile.html")



# ============================
# Blog Post CRUD Views
# ============================

# List all posts (open to everyone)
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]


# Show a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


# Create new post (authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update a post (only the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("posts")

    def test_func(self):
        return self.get_object().author == self.request.user


# Delete a post (only the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("posts")

    def test_func(self):
        return self.get_object().author == self.request.user
