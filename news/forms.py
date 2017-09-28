from django import forms
from .models import Post, Comments
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class NewsFilterForm(forms.Form):
    ordering = forms.ChoiceField(label="sort", required=False, choices=[
        ["title", "from A-Z"]
    ])

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentFrom(ModelForm):
    class Meta:
        model = Comments
        fields = ('comments_text',)
