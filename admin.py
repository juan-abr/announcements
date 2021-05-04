from django.contrib import admin

from .models import Announcement, Event, EventRegistration, Media

# Register your models here.
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    # list_display = ('title',)
    ordering     = ('-pub_date',)
    # search_fields = ('title',)
    list_filter = ('pub_date',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # list_display = ('announcement',)
    ordering     = ('-event_date',)
    # search_fields = ('announcement',)
    list_filter = ('event_date',)
    
@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'user')
    list_filter = ('event', 'user')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'announcement')

# admin.site.register(Announcement)
# admin.site.register(Event)
# admin.site.register(EventRegistration)