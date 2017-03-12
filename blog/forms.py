from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ("published_date", "user",)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ("published_date", "user", "post",)
