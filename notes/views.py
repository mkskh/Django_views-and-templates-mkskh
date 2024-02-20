"""Views for the notes app."""
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.views import View
from django.views.generic import TemplateView

from notes.models import notes


def redirect_to_note_detail(request, note_id):
    """Redirect to the note details view."""
    return redirect(reverse("notes:details", args=[note_id]))


def home(request):
    """Home for my notes app."""
    template = get_template('notes/notes_page.html')
    context = {
        'sections_url': reverse('notes:sections'),
        'first_note_url': reverse('notes:details', args=[1]),
    }
    rendered_template = template.render(context, request)
    return HttpResponse(rendered_template)


class SectionsView(View):

    def get(self, request):
        """Show the list of note sections."""
        template = get_template('notes/sections.html')
        context = {
            'web_framework': reverse("notes:by_section", args=["Web Frameworks"]),
            'set_up_dj': reverse("notes:by_section", args=["Setting up Django"]),
            'url_map': reverse("notes:by_section", args=["URL Mapping"]),
            'back_home': reverse("notes:home")
        }
        rendered_template = template.render(context, request)
        return HttpResponse(rendered_template)


class BySectionView(View):

    def get(self, request, section_name):
        """Show the notes of a section."""
        template = get_template('notes/by_section.html')
        notes_for_section = self._get_note_items_by_section(section_name)
        context = {
            'section_name': section_name,
            'notes': notes_for_section,
            'back_sections': reverse("notes:sections"),
        }
        rendered_template = template.render(context, request)
        return HttpResponse(rendered_template)


    def _get_note_items_by_section(self, section_name):
        """Return the notes of a section as list items."""
        return [f"{note['text']}" for note in notes
                if note["section"] == section_name]


class NoteDetails(TemplateView):
    """Note details."""

    template_name = "notes/details.html"

    def get_context_data(self, note_id):
        """Return the note data."""
        return {
            "id": note_id,
            "num_notes": len(notes),
            "note": notes[note_id - 1],
            'next_note': note_id + 1 if note_id < len(notes) else None,
            'previous_note': note_id - 1 if note_id > 1 else None,
        }


class SearchResultsView(TemplateView):
    """Execute the search and show results."""

    template_name = "notes/search.html"

    def get_context_data(self, search_term):
        """Return the term and list of notes."""
        result = [(note['section'], note['text']) for note in notes if search_term.lower() in note['text'].lower()]
        return {
            "term": search_term,
            "result": result,
        }