from django.contrib import admin
from .models import Note

# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Admin configuration for the Note model."""
    list_display = ("title", "color", "created_at", "updated_at")
    search_fields = ("title", "content")
    list_filter = ("color", "created_at")
