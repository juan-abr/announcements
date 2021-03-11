from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView

from .models import Event

# Create your views here.
class EventArchiveIndexView(ArchiveIndexView):
    model = Event
    date_field = 'event_date'