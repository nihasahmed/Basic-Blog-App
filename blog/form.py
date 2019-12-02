
from django import forms
from .models import Post


class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'pic', 'content', 'user_id']

    def __init__(self, *args, **kwargs):
        super(BlogPost, self).__init__(*args, **kwargs)
        self.fields['pic'].required = False
        self.fields['user_id'].required = False