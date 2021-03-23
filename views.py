
from django.shortcuts import render, redirect
from django.http import Http404
from django.utils.timezone import now
from django.views.generic.dates import ArchiveIndexView, MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Announcement, Event, EventRegistration

# Create your views here.
# class EventArchiveIndexView(ArchiveIndexView):
#     model = Event
#     date_field = 'event_date'

class AnnouncementMonthView(MonthArchiveView):
    def get_month(self):
        try:
            month = super(AnnouncementMonthView, self).get_month()
        except Http404:
            month = now().strftime(self.get_month_format())
        return month
    def get_year(self):
        try:
            month = super(AnnouncementMonthView, self).get_year()
        except Http404:
            year = now().strftime(self.get_year_format())
        return year

    model = Announcement
    date_field = 'pub_date'
    allow_future = True

class EventMonthView(LoginRequiredMixin, MonthArchiveView):
    def get_month(self):
        try:
            month = super(EventMonthView, self).get_month()
        except Http404:
            month = now().strftime(self.get_month_format())
        return month
    def get_year(self):
        try:
            month = super(EventMonthView, self).get_year()
        except Http404:
            year = now().strftime(self.get_year_format())
        return year

    model = Event
    date_field = 'event_date'
    allow_future = True

def event_add_attendance(request, pk):
    this_event = Events.objects.get(pk=pk)
    this_event.add_user_to_list_of_attendees(user = request.user)
    return redirect('announcements:event_month', pk=pk)