from django.shortcuts import render, get_object_or_404
from .models import Note
from .forms import NoteForm, ContactForm

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()

    return render(request, "notes/notes_list.html", {"notes": notes})


def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    return render(request, "notes/notes_detail.html", {"note": note})


# The following three view functions use NoteForm and ContactForm
def add_note(request):
    # Some stuff needs to go here

    return render(request, "notes/add_note.html", {"form": form})


def edit_note(request, pk):
    # Some stuff needs to go here

    return render(request, "notes/edit_note.html", {"form": form})


def contact_us(request):
    if request.method == "GET":
        form = ContactForm()

    else:
        form = ContactForm(data=request.POST)

        respond_email = form.cleaned_data['email']
        message_body = form.cleaned_data['body']

        # Email the user that their message was received and email the admin the user's message

    return render(request, "notes/contact_us.html", {"form": form})