from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, mail_admins
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from .models import Poem, Comment
from .forms import PoemForm, CommentForm, ContactForm, SearchForm


# Create your views here.
def poems_list(request):
    poems = Poem.objects.all()

    return render(request, "poems/poems_list.html", {"poems": poems})


def poems_detail(request, pk):
    # NOTE: this view doubles as the endpoint for adding comments
    poem = get_object_or_404(Poem, pk=pk)
    comments = poem.comments

    if request.method == "GET":
        form = CommentForm()

    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.poem = poem  # Make sure the comment is linked to the Poem instance connected to this detail view
            comment.save()  # Save the new comment instance
            success(request, "Comment saved!")

            
            return redirect(to="poems_detail", pk=poem.pk)

        else:
            error(request, "Couldn't save comment :(")

    # This return statement will be the exit point from the view function if the method was GET or validation failed
    return render(request, "poems/poems_detail.html", {"poem": poem, "comments": comments, "form": form})


@login_required
def add_poem(request):
    if request.method == "GET":
        form = PoemForm()

    else:
        form = PoemForm(data=request.POST)

        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = request.user # associate the new poem with the currently signed in user
            poem.save()
 
            success(request, "Your poem was created!")

            return redirect(to="poems_list")

        else:
            error(request, "Your poem could not be created :(")

    return render(request, "poems/add_poem.html", {"form": form})


@login_required
def edit_poem(request, pk):
    poem = get_object_or_404(Poem, pk=pk)

    if request.method == "GET":
        form = PoemForm(instance=poem)

    else:
        form = PoemForm(data=request.POST, instance=poem)

        if form.is_valid():
            form.save()  # We can save the form directly since the instance has already been created

            success(request, "Your poem was updated! Great work!")

            return redirect(to="poems_detail", pk=pk)

        else:
            error(request, "Your updates didn't work :(")

    return render(request, "poems/edit_poem.html", {"form": form})


@login_required
def delete_poem(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    poem.delete()
    success(request, "Your poem was deleted. Sorry you didn't like it <3.")

    return redirect(to="poems_list")


def contact(request):
    if request.method == "GET":
        form = ContactForm()

    else:
        form = ContactForm(data=request.POST)

        if form.is_valid():
            user_email = form.cleaned_data['email']
            message_title = form.cleaned_data['title']
            message_body = form.cleaned_data['body']

            send_mail("Poems - Your message has been sent", "Your message has been sent! Expect to hear from an admin soon!", recipient_list=[user_email])
            mail_admins(message_title, message_body, fail_silently=True)

            success(request, "Your message was sent. Check your email for confirmation.")

            return redirect(to="poems_list")

        else:
            error("Your message couldn't be sent :(.")

    return render(request, "contact.html", {"form": form})


def search(request):
    if request.method == "GET":
        form = SearchForm()

    else:
        form = SearchForm(data=request.POST)

        if form.is_valid():
            poems = Poem.objects.all()
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            order_by = form.cleaned_data['order_by']

            if title:
                title_search_type = form.cleaned_data['title_search_type']

                if title_search_type == "starts with":
                    poems = poems.filter(title__startswith=title)

                elif title_search_type == "includes":
                    poems = poems.filter(title__contains=title)

                else:
                    poems = poems.filter(title__exact=title)

            if body:
                poems = poems.filter(body__contains=body)
            
            """
                body_search_type = form.cleaned_data['body_search_type']

                if body_search_type == "starts with":
                    poems = poems.filter(body__startswith=body)

                elif body_search_type == "includes":
                    poems = poems.filter(body__contains=body)

                else:
                    poems = poems.filter(body__exact=body)
            """

            poems = poems.order_by(order_by)

            return render(request, "poems/search_results.html", {"poems": poems})

    return render(request, "poems/search.html", {"form": form})
