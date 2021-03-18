from django.db import models

# Create your models here.
class Announcement(models.Model):
    title       = models.CharField(max_length = 100)
    desc        = models.TextField(blank=True)
    pub_date    = models.DateField()             # Day Event is Posted (for newsletter)
    recurring   = models.BooleanField()          # If true, the event repeats every week

    event_date  = models.DateField(blank=True, null=True)             # Day of the Event

    def __str__(self):
        return self.title