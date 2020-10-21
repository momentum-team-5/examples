from django import forms
from .models import Poem, Comment


class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = [
            'title',
            'body'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body'
        ]


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    title = forms.CharField(max_length=255)
    body = forms.CharField(required=True, widget=forms.Textarea)
