from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from django.views.generic import ListView
from datetime import date

from .views import *
from .models import Announcement

urlpatterns = [
    path('', AnnouncementMonthArchiveView.as_view(), name="show_events"),

    path('list/', ListView.as_view(model=Announcement), name='announcement_list'),
    path('archive/', ArchiveIndexView.as_view(model=Announcement, date_field="announcement_date", allow_future=True), name="announcement_archive"),

    # Example: /2012/08/
    path('<int:year>/<int:month>/', EventMonthArchiveView.as_view(month_format='%m'), name="archive_month_numeric"),
    # Example: /2012/aug/
    path('<int:year>/<str:month>/', EventMonthArchiveView.as_view(), name="archive_month"),
]