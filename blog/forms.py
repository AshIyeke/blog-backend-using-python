from django import forms
from .models import Comment

# Form to share a post via email
class EmailPostForm(forms.Form):
 name = forms.CharField(max_length=25)
 email = forms.EmailField()
 to = forms.EmailField()
 comments = forms.CharField(required=False,
 widget=forms.Textarea)

# Form to add a comment to a post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')