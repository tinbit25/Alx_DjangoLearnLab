# blog/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
from django import forms
from .models import Post
from taggit.forms import TagWidget  # This is necessary to create the Tag widget

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=TagWidget()  # This adds a tag input widget
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' in the form fields
