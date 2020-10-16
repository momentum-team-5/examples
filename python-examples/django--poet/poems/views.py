from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Poem, Comment
from .forms import PoemForm, CommentForm


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
            return redirect(to="poems_list")

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