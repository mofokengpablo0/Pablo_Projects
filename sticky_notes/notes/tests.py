# notes/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Note
from .forms import NoteForm


class NoteModelTest(TestCase):
    """
    Tests for the Note model.
    Verifies that Note objects are created correctly and behave as expected.
    """

    def setUp(self):
        """
        setUp runs before every test method.
        We use it to create a Note object that the tests can use.
        """
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
            color="#fff9a8",
        )

    def test_note_has_title(self):
        """Test that a Note object has the expected title."""
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        """Test that a Note object has the expected content."""
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.content, "This is a test note.")

    def test_note_has_color(self):
        """Test that a Note object has the expected default colour."""
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.color, "#fff9a8")

    def test_note_string_representation(self):
        """Test that __str__ returns the note's title."""
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(str(note), "Test Note")

    def test_note_get_absolute_url(self):
        """Test that get_absolute_url returns the correct detail URL."""
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.get_absolute_url(), f"/note/{note.id}/")

    def test_note_created_at_is_set(self):
        """Test that created_at is automatically set on creation."""
        note = Note.objects.get(id=self.note.id)
        self.assertIsNotNone(note.created_at)

    def test_note_updated_at_is_set(self):
        """Test that updated_at is automatically set on creation."""
        note = Note.objects.get(id=self.note.id)
        self.assertIsNotNone(note.updated_at)


class NoteListViewTest(TestCase):
    """Tests for the note_list view (the home page)."""

    def setUp(self):
        """Create a test note before each test runs."""
        self.note = Note.objects.create(
            title="My Test Note",
            content="Test content for the list view.",
        )

    def test_note_list_view_status_code(self):
        """Test that the home page returns HTTP 200 (OK)."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)

    def test_note_list_view_uses_correct_template(self):
        """Test that the home page uses note_list.html."""
        response = self.client.get(reverse("note_list"))
        self.assertTemplateUsed(response, "notes/note_list.html")

    def test_note_list_view_displays_note(self):
        """Test that the home page displays the note's title."""
        response = self.client.get(reverse("note_list"))
        self.assertContains(response, "My Test Note")

    def test_note_list_view_displays_content(self):
        """Test that the home page displays the note's content."""
        response = self.client.get(reverse("note_list"))
        self.assertContains(response, "Test content for the list view.")

    def test_note_list_view_empty_state(self):
        """Test that the home page shows an empty state when no notes exist."""
        # Delete the note created in setUp
        Note.objects.all().delete()
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No sticky notes yet")


class NoteDetailViewTest(TestCase):
    """Tests for the note_detail view (single note page)."""

    def setUp(self):
        """Create a test note before each test runs."""
        self.note = Note.objects.create(
            title="Detail Test Note",
            content="Content for the detail view test.",
        )

    def test_note_detail_view_status_code(self):
        """Test that the detail page returns HTTP 200 (OK)."""
        response = self.client.get(
            reverse("note_detail", args=[self.note.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_note_detail_view_uses_correct_template(self):
        """Test that the detail page uses note_detail.html."""
        response = self.client.get(
            reverse("note_detail", args=[self.note.id])
        )
        self.assertTemplateUsed(response, "notes/note_detail.html")

    def test_note_detail_view_displays_title(self):
        """Test that the detail page shows the note's title."""
        response = self.client.get(
            reverse("note_detail", args=[self.note.id])
        )
        self.assertContains(response, "Detail Test Note")

    def test_note_detail_view_displays_content(self):
        """Test that the detail page shows the note's content."""
        response = self.client.get(
            reverse("note_detail", args=[self.note.id])
        )
        self.assertContains(response, "Content for the detail view test.")

    def test_note_detail_view_404_for_invalid_id(self):
        """Test that requesting a non-existent note returns 404."""
        response = self.client.get(reverse("note_detail", args=[9999]))
        self.assertEqual(response.status_code, 404)


class NoteCreateViewTest(TestCase):
    """Tests for the note_create view (creating a new note)."""

    def test_note_create_view_get_status_code(self):
        """Test that GET request to the create page returns 200."""
        response = self.client.get(reverse("note_create"))
        self.assertEqual(response.status_code, 200)

    def test_note_create_view_uses_correct_template(self):
        """Test that the create page uses note_form.html."""
        response = self.client.get(reverse("note_create"))
        self.assertTemplateUsed(response, "notes/note_form.html")

    def test_note_create_view_post_creates_note(self):
        """Test that POSTing valid data creates a new note."""
        response = self.client.post(
            reverse("note_create"),
            {
                "title": "Newly Created Note",
                "content": "This note was created via a test.",
                "color": "#a8e6cf",
            },
        )
        # Should redirect to note_list after successful creation
        self.assertEqual(response.status_code, 302)
        # Verify the note was saved to the database
        self.assertTrue(Note.objects.filter(
            title="Newly Created Note").exists())

    def test_note_create_view_post_invalid_data(self):
        """Test that POSTing invalid data does NOT create a note."""
        response = self.client.post(
            reverse("note_create"),
            {
                "title": "",  # Empty title - should fail validation
                "content": "Content without a title",
                "color": "#fff9a8",
            },
        )
        # Should re-render the form (status 200, not redirect)
        self.assertEqual(response.status_code, 200)
        # Verify no note was created
        self.assertEqual(Note.objects.count(), 0)


class NoteUpdateViewTest(TestCase):
    """Tests for the note_update view (editing an existing note)."""

    def setUp(self):
        """Create a test note before each test runs."""
        self.note = Note.objects.create(
            title="Original Title",
            content="Original content.",
        )

    def test_note_update_view_get_status_code(self):
        """Test that GET request to the edit page returns 200."""
        response = self.client.get(
            reverse("note_update", args=[self.note.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_note_update_view_uses_correct_template(self):
        """Test that the edit page uses note_form.html."""
        response = self.client.get(
            reverse("note_update", args=[self.note.id])
        )
        self.assertTemplateUsed(response, "notes/note_form.html")

    def test_note_update_view_post_updates_note(self):
        """Test that POSTing valid data updates the existing note."""
        response = self.client.post(
            reverse("note_update", args=[self.note.id]),
            {
                "title": "Updated Title",
                "content": "Updated content.",
                "color": "#ffb3b3",
            },
        )
        # Should redirect to note_list after successful update
        self.assertEqual(response.status_code, 302)
        # Refresh the note from the database and check the new values
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")
        self.assertEqual(self.note.content, "Updated content.")
        self.assertEqual(self.note.color, "#ffb3b3")

    def test_note_update_view_404_for_invalid_id(self):
        """Test that updating a non-existent note returns 404."""
        response = self.client.get(reverse("note_update", args=[9999]))
        self.assertEqual(response.status_code, 404)


class NoteDeleteViewTest(TestCase):
    """Tests for the note_delete view (deleting a note)."""

    def setUp(self):
        """Create a test note before each test runs."""
        self.note = Note.objects.create(
            title="Note to Delete",
            content="This note will be deleted.",
        )

    def test_note_delete_view_get_status_code(self):
        """Test that GET request shows the confirmation page."""
        response = self.client.get(
            reverse("note_delete", args=[self.note.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_note_delete_view_uses_correct_template(self):
        """Test that the delete page uses note_confirm_delete.html."""
        response = self.client.get(
            reverse("note_delete", args=[self.note.id])
        )
        self.assertTemplateUsed(response, "notes/note_confirm_delete.html")

    def test_note_delete_view_post_deletes_note(self):
        """Test that POSTing to the delete URL removes the note."""
        response = self.client.post(
            reverse("note_delete", args=[self.note.id])
        )
        # Should redirect to note_list after deletion
        self.assertEqual(response.status_code, 302)
        # Verify the note is gone from the database
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())

    def test_note_delete_view_404_for_invalid_id(self):
        """Test that deleting a non-existent note returns 404."""
        response = self.client.get(reverse("note_delete", args=[9999]))
        self.assertEqual(response.status_code, 404)


class NoteFormTest(TestCase):
    """Tests for the NoteForm."""

    def test_note_form_valid_data(self):
        """Test that the form is valid with complete data."""
        form = NoteForm(
            data={
                "title": "Form Test Note",
                "content": "Testing the form's validation.",
                "color": "#b3d9ff",
            }
        )
        self.assertTrue(form.is_valid())

    def test_note_form_missing_title(self):
        """Test that the form is invalid without a title."""
        form = NoteForm(
            data={
                "title": "",
                "content": "Content without a title",
                "color": "#fff9a8",
            }
        )
        self.assertFalse(form.is_valid())

    def test_note_form_missing_content(self):
        """Test that the form is invalid without content."""
        form = NoteForm(
            data={
                "title": "Title without content",
                "content": "",
                "color": "#fff9a8",
            }
        )
        self.assertFalse(form.is_valid())

    def test_note_form_blank(self):
        """Test that an empty form is invalid."""
        form = NoteForm(data={})
        self.assertFalse(form.is_valid())


class NoteUrlTest(TestCase):
    """Tests for URL routing."""

    def test_note_list_url_resolves(self):
        """Test that the home URL routes to the note_list view."""
        url = reverse("note_list")
        self.assertEqual(url, "/")

    def test_note_detail_url_resolves(self):
        """Test that the detail URL includes the note's ID."""
        url = reverse("note_detail", args=[1])
        self.assertEqual(url, "/note/1/")

    def test_note_create_url_resolves(self):
        """Test that the create URL is /note/new/."""
        url = reverse("note_create")
        self.assertEqual(url, "/note/new/")

    def test_note_update_url_resolves(self):
        """Test that the update URL includes the note's ID."""
        url = reverse("note_update", args=[1])
        self.assertEqual(url, "/note/1/edit/")

    def test_note_delete_url_resolves(self):
        """Test that the delete URL includes the note's ID."""
        url = reverse("note_delete", args=[1])
        self.assertEqual(url, "/note/1/delete/")
