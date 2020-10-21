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
    title = forms.CharField(max_length=255)
    body = forms.CharField(required=True, widget=forms.Textarea)


class SearchForm(forms.Form):
    # This tuple will be used to implement different search types
    SEARCH_TYPES_CHOICES = (
        ("starts with", "starts with"),
        ("includes", "includes"),
        ("exact match", "exact match"),
    )

    # This tuple provides selections for ordering the results
    ORDER_CHOICES = (
        ("title", "title"),
        ("body", "body"),
    )

    # Form fields
    title = forms.CharField(max_length=255)
    title_search_type = forms.ChoiceField(choices=SEARCH_TYPES_CHOICES, label="search title for", widget=forms.RadioSelect, required=True)
    body = forms.CharField(widget=forms.Textarea)
    body_search_type = forms.ChoiceField(choices=SEARCH_TYPES_CHOICES, label="search body for", widget=forms.RadioSelect, required=True)
    order_by = forms.ChoiceField(choices=ORDER_CHOICES, widget=forms.RadioSelect, required=True)

    def clean(self):
        """
        Require at least one of title and body to be non-blank.
        """
        cleaned_data = super().clean()
        cleaned_title = cleaned_data['title']
        cleaned_body = cleaned_data['body']

        if cleaned_title or cleaned_body:
            return cleaned_data

        raise ValidationError('At least one search field must be specified', code='invalid')
