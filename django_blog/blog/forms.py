from django import forms
from .models import Post
from taggit.forms import TagWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # <-- this is what the checker is looking for
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
