from django import forms

from .models import Comment,Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'email', 'body')