from django import forms
from django.forms import ModelForm
from .models import EventRegistration

class EventRegistrationForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = EventRegistration
        fields = '__all__'