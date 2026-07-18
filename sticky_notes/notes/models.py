from django.db import models
from django.urls import reverse

# Create your models here.


class Note(models.Model):
    """Model representing a sticky note.

    Fields:
    - title: CharField for the note's title.
    - content: TextField for the note's content.
    - color: CharField to choose background color (sticky note style).
    - created_at: DateTimeField when the note was created.
    - updated_at: DateTimeField when the note was last updated.

    Methods:
    - __str__: Returns a string representation of the note.
    - get_absolute_url: Returns the URL to view the note's details.
    """
    COLOR_CHOICES = [
        ("#fff9a8", "Yellow"),
        ("#a8e6cf", "Green"),
        ("#ffb3b3", "Pink"),
        ("#b3d9ff", "Blue"),
        ("#d9b3ff", "Purple"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    color = models.CharField(
        max_length=7, choices=COLOR_CHOICES, default="#fff9a8"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Note object (in Admin site etc.)."""
        return self.title

    def get_absolute_url(self):
        """Return a string representation of the note object (in Admin site etc.)."""
        return reverse("note_detail", kwargs={"pk": self.pk})
