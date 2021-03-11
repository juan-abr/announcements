from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from django.views.generic import ListView

# from .views import *
from .models import Event

urlpatterns = [
    path('archive/', ArchiveIndexView.as_view(model=Event, date_field="event_date"), name="event_archive"),
    path('list/', ListView.as_view(model=Event), name='event_list'),
]