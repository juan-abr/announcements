from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from django.views.generic import ListView
from datetime import date

from .views import *
# from . import views
from .models import Announcement

app_name = 'announcements'

urlpatterns = [
    path('', AnnouncementMonthView.as_view(), name="show_announcements"),
    path('events/', EventMonthView.as_view(), name="show_events"),
    path('events/registration/edit/<int:pk>', EventRegistrationView.as_view(), name='event_registration_update'),
    path('events/registration/add/<int:pk>', event_add_attendance, name = 'event_registration_create'),

    path('list/', ListView.as_view(model=Announcement), name='announcement_list'),
    path('archive/', ArchiveIndexView.as_view(model=Announcement, date_field="announcement_date", allow_future=True), name="announcement_archive"),

    # Example: /2012/08/
    path('<int:year>/<int:month>/', AnnouncementMonthView.as_view(month_format='%m'), name="announcement_month_numeric"),
    # Example: /2012/aug/
    path('<int:year>/<str:month>/', AnnouncementMonthView.as_view(), name="announcement_month"),

    # Example: /2012/08/
    path('events/<int:year>/<int:month>/', EventMonthView.as_view(month_format='%m'), name="event_month_numeric"),
    # Example: /2012/aug/
    path('events/<int:year>/<str:month>/', EventMonthView.as_view(), name="event_month"),
]