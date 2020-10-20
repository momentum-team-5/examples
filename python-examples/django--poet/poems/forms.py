from django import forms
from .models import Poem, Comment


class PoemForm(forms.ModelForm):
    """
    Model form for the Poem class used for create and update operations.
    """
    class Meta:
        model = Poem
        fields = [
            'title',
            'body'
        ]


class CommentForm(forms.ModelForm):
    """
    Model form for the Comment class supporting create and update operations.
    """
    class Meta:
        model = Comment
        fields = [
            'body'
        ]


class ContactForm(forms.Form):
    """
    A simple contact form.
    """
    email = forms.EmailField(required=True)
    title = forms.CharField(required=True, max_length=255)
    body = forms.CharField(label="Your messsage", widget=forms.Textarea(attrs={'required': True}))
