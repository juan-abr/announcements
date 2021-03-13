from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView, MonthArchiveView

from .models import Event

# Create your views here.
# class EventArchiveIndexView(ArchiveIndexView):
#     model = Event
#     date_field = 'event_date'

class EventMonthArchiveView(MonthArchiveView):
    model = Event
    date_field = 'event_date'
    allow_future = True