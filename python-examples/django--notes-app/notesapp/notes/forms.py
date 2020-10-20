from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body'
        ]


class ContactForm(forms.Form):
    email = forms.EmailField()
    body = forms.Textarea()
