from django.db import models
# This is django's builtin user class
from django.contrib.auth.models import User

class Comment(models.Model):
    """
    An anonymous comment on a poem.
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    poem = models.ForeignKey('Poem', on_delete=models.CASCADE)

    def render_html(self):
        return f"""
        <div class='poem-comment-container'>
            <p class='timestamp'>Comment on ({self.timestamp}): <pre>{self.body}</pre></p>
        </div>
        """

# Create your models here.
class Poem(models.Model):
    """
    Represents a single poem.
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def comments(self):
        return Comment.objects.filter(poem=self)

    def render_html(self):
        return f"""
        <div class='poem-container'>
            <h4>{self.title}</h4>
            <p class='poem-author'>{self.author}</p>
            <p class='poem-body'>{self.body}</p>
        </div>
        """