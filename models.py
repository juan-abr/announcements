from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Announcement(models.Model):
    title       = models.CharField(max_length = 100)
    desc        = models.TextField(blank=True)
    pub_date    = models.DateField()             # Day Event is Posted (for newsletter)
    recurring   = models.BooleanField()          # If true, the event repeats every week

    #event_date  = models.DateField(blank=True, null=True)             # Day of the Event

    def __str__(self):
        return '%s announced %s' % (self.title, str(self.pub_date.strftime("%Y-%m-%d")))

    @property
    def media(self):
        return self.media_set.all()

class Event(models.Model):
    announcement    = models.OneToOneField(Announcement, on_delete=models.CASCADE)
    event_date      = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.announcement

    def add_user_to_list_of_attendees(self, user):
        registration = EventRegistration.objects.create(user = user, event = self)
        return registration.pk

class EventRegistration(models.Model):
    event   = models.ForeignKey(Event, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Attendee')
    number  = models.IntegerField(verbose_name='Number of Guests', default=1)
    note   = models.TextField(blank = True)

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('announcements:event_registration_update', args=[self.pk])

class Media(models.Model):
    file_name       = models.CharField(max_length = 50)
    announcement    = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    desc            = models.TextField(blank = True)
    position        = models.IntegerField(blank=True)

    def __str__(self):
        return self.file_name