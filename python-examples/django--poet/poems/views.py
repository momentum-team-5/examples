from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, mail_admins
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from .models import Poem, Comment
from .forms import PoemForm, CommentForm, ContactForm


# Create your views here.
def poems_list(request):
    """
    A list of all poems (anyone can view these).
    """
    poems = Poem.objects.all()

    return render(request, "poems/poems_list.html", {"poems": poems})


def poems_detail(request, pk):
    """
    Detailed view of a particular poem.
    """
    poem = get_object_or_404(Poem, pk=pk)

    return render(request, "poems/poems_detail.html", {"poem": poem})


@login_required
def poems_create(request):
    """
    Create a new poem.
    """
    if request.method == "GET":
        form = PoemForm()

    else:
        form = PoemForm(data=request.POST)

        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = request.user
            poem.save()
            success(request, "Poem added.")
            return redirect(to="poems_list")

        else:
            error(request, "Problem with your submission.")


    return render(request, "poems/poems_create.html", {"form": form})


@login_required
def poems_update(request, pk):
    """
    Update an existing poem.
    """
    poem = get_object_or_404(Poem, pk=pk)

    if request.method == "GET":
        form = PoemForm(instance=poem)

    else:
        form = PoemForm(data=request.POST, instance=poem)

        if form.is_valid():
            form.save()
            return redirect(to="poems_list")

    return render(request, "poems/poems_update.html", {"form": form})


@login_required
def poems_delete(request, pk):
    """
    Delete a particular poem.
    """
    poem = get_object_or_404(Poem, pk=pk)
    poem.delete()
    return redirect(to="poems_list")


def add_comment(request, pk):
    """
    .
    """
    poem = get_object_or_404(Poem, pk=pk)

    if request.method == "GET":
        form = CommentForm()

    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.poem = poem
            comment.save()

            return redirect(to='poems_list')

    return render(request, "poems/add_comment.html", {"form": form, "poem": poem })


def contact(request):
    if request.method == "GET":
        form = ContactForm()

    else:
        form = ContactForm(data=request.POST)

        if form.is_valid():
            send_confirmation_to = form.cleaned_data['email']
            message_title = form.cleaned_data['title']
            message_body = form.cleaned_data['body']

            send_mail("Your message was received", "Your message was received. Expect a response shortly!", recipient_list=[send_confirmation_to])
            mail_admins(message_title, message_body, fail_silently=True)

            return redirect(to='poems_list')

    return render(request, "contact_us.html", {"form": form})
