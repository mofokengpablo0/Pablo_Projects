from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating Note objects.

    Fields:
    - title: CharField for the note's title.
    - content: TextField for the note's content.
    - color: ChoiceField for the note's background color.

    Meta class:
    - Defines the model to use (Note) and the fields to include in the form.
    """

    class Meta:
        model = Note
        fields = ["title", "content", "color"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter title..."}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Write your note here..."}),
            "color": forms.Select(attrs={"class": "form-control"}),
        }
