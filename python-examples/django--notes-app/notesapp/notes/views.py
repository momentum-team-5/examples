from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages import success, error
from .models import Note
from .forms import NoteForm


# Create your views here.
def notes_list(request):
    notes = Note.objects.all()

    return render(request, "notes/notes_list.html", {"notes": notes})


def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    return render(request, "notes/notes_detail.html", {"note": note})


# The following three view functions use NoteForm and ContactForm
def add_note(request):
    if request.method == "GET":
        form = NoteForm()

    else:
        form = NoteForm(data=request.POST)

        if form.is_valid():
            form.save()
            success(request, "Note added!")
            redirect(to="notes_list")

        else:
            error(request, "Could not add note :( .")

    return render(request, "notes/add_note.html", {"form": form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == "GET":
        form = NoteForm(instance=note)

    else:
        form = NoteForm(data=request.POST, instance=note)

        if form.is_valid():
            form.save()
            success(request, "Note updated!")
            redirect(to="notes_list")

        else:
            error(request, "Could not update note :( .")

    return render(request, "notes/edit_note.html", {"form": form})


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    success(request, "Note deleted!")

    return redirect(to="notes_list")


def contact_us(request):
    return redirect(to="notes_list")
