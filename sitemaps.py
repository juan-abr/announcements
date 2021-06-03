from django.contrib.sitemaps import Sitemap

from .models import Announcement, Event

class AnnouncementSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Announcement.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.Announcement.pub_date