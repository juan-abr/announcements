from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.utils.timezone import now
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.dates import ArchiveIndexView, MonthArchiveView
from django.views.generic import CreateView, UpdateView

from .models import Announcement, Event, EventRegistration
from .forms import EventRegistrationForm

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

# def event_add_attendance(request, *args, **kwargs):
def event_add_attendance(request, event_pk):
    # pk = kwargs.get('pk')
    this_event = Event.objects.get(pk=event_pk)
    this_event.add_user_to_list_of_attendees(user = request.user)
    # new_object = EventRegistration.objects.get(pk=pk)
    registration = get_object_or_404(EventRegistration, pk)
    # return redirect('announcements:event_registration_update', pk=pk)
    # return redirect('announcements:show_events')
    return redirect(registration)
    # return redirect('event_registration_update.html', pk=pk)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('announcements:login')
    template_name = 'registration/signup.html'

class EventRegistrationView(UpdateView):
    model = EventRegistration
    fields = ['number']
    # form_class = EventRegistrationForm
    success_url = reverse_lazy('announcements:show_events')
    template_name_suffix = '_update'

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)