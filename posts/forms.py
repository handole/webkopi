from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "harga",
            "link_BL",
            "image",
            "draft",
            "publish",
        ]
