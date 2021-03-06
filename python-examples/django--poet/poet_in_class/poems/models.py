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


# Create your models here.
class Poem(models.Model):
    """
    Represents a single poem.
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name="favorites")

    @property
    def comments(self):
        return Comment.objects.filter(poem=self)

    def numfavorites(self):
        return self.favorites.all().count()