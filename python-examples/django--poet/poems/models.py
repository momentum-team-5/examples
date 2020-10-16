from django.db import models
from users.models import User



class Comment(models.Model):
    """
    Represents a comment written about a poem.
    """
    timestamp = models.DateTimeField(auto_now=True)
    body = models.TextField(null=True, blank=True)
    poem = models.ForeignKey("Poem", on_delete=models.CASCADE)

# Create your models here.
class Poem(models.Model):
    """
    Represents a poem written by a registered user.
    """
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def comments(self):
        """
        Get the comments associated with this poem.
        """
        return Comment.objects.filter(poem=self)
