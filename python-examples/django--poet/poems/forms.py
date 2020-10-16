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
