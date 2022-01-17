from socket import fromshare
from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ('quote',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quote'].widget.attrs.update({"class": "form-control"})

class CommentForm(forms.ModelForm):
    class Metal:
        model= Comment
        fields =('text',)