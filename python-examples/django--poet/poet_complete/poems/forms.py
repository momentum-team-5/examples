from django import forms
from django.core.exceptions import ValidationError
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
    message_title = forms.CharField(max_length=255)
    message_body = forms.CharField(required=True, widget=forms.Textarea)


class SearchForm(forms.Form):
    # This tuple provides selections for ordering the results
    ORDER_CHOICES = (
        ("title", "title"),
        ("body", "body"),
    )

    # Form fields
    title = forms.CharField(max_length=255, required=True)
    order_by = forms.ChoiceField(choices=ORDER_CHOICES, widget=forms.RadioSelect, required=True)
