from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse

# Create your models here.
class Announcement(models.Model):
    title       = models.CharField(max_length = 100)
    desc        = models.TextField(blank=True)
    pub_date    = models.DateField()             # Day Event is Posted (for newsletter)
    recurring   = models.BooleanField()          # If true, the event repeats every week

    #event_date  = models.DateField(blank=True, null=True)             # Day of the Event

    def __str__(self):
        return '%s %s' % (str(self.pub_date.strftime("%Y-%m-%d")), self.title)

class Event(models.Model):
    announcement    = models.OneToOneField(Announcement, on_delete=models.CASCADE)
    event_date      = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.announcement

class EventRegistration(models.Model):
    event   = models.ForeignKey(Event, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Atendee')
    number  = models.IntegerField(verbose_name='Number of Guests')

    def __str__(self):
        return self.user.last_name + ", " + self.user.first_name

def add_user_to_list_of_attendees(self, user):
    registration = EventRegistration.objects.create(user = user, event = self)