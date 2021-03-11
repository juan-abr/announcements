from django.db import models

# Create your models here.
class Event(models.Model):
    title       = models.CharField(max_length = 100)
    desc        = models.TextField(blank=True)
    event_date  = models.DateField()             # Day of the Event
    pub_date    = models.DateField()             # Day Event is Posted
    recurring   = models.BooleanField()          # If true, the event repeats every week

    def __str__(self):
        return self.title