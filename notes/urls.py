"""Notes URL Configuration."""
from django.urls import path
from .views import SectionsView, BySectionView, NoteDetails, SearchResultsView

from notes.views import home

app_name = "notes"
urlpatterns = [
    path('', home, name="home"),
    path('sections/', SectionsView.as_view(), name="sections"),
    path('sections/<section_name>/', BySectionView.as_view(), name="by_section"),
    path('<int:note_id>/', NoteDetails.as_view(), name="details"),
    path('<str:search_term>/', SearchResultsView.as_view(), name="search"),
]
