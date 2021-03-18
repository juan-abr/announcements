
from django.shortcuts import render
from django.http import Http404
from django.utils.timezone import now
from django.views.generic.dates import ArchiveIndexView, MonthArchiveView

from .models import Announcement

# Create your views here.
# class EventArchiveIndexView(ArchiveIndexView):
#     model = Event
#     date_field = 'event_date'

class AnnouncementMonthArchiveView(MonthArchiveView):
    def get_month(self):
        try:
            month = super(AnnouncementMonthArchiveView, self).get_month()
        except Http404:
            month = now().strftime(self.get_month_format())
        return month
    def get_year(self):
        try:
            month = super(AnnouncementMonthArchiveView, self).get_year()
        except Http404:
            year = now().strftime(self.get_year_format())
        return year

    model = Announcement
    date_field = 'pub_date'
    allow_future = True

class EventMonthArchiveView(MonthArchiveView):
    model = Announcement
    date_field = 'event_date'
    allow_future = True