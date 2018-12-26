from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event
from django import forms

class EventForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Event
        fields = '__all__'

