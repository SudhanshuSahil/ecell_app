from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event
from django import forms
from venue.models import Venue

class EventForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    venue = forms.ModelChoiceField(queryset=Venue.objects.all(), widget=forms.Select, empty_label=None)
    class Meta:
        model = Event
        fields = '__all__'

# class EventsChoices(forms.ModelForm):
#     events = forms.ModelChoiceField(queryset=Event.objects.all(), widget=forms.Select, empty_label=None)
#     class Meta:
#         fields = 'events'
