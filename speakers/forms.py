from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Speaker
from django import forms


class SpeakerForm(forms.ModelForm):
    # start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    # date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    # venue = forms.ModelChoiceField(queryset=Venue.objects.all(), widget=forms.Select, empty_label=None)
    class Meta:
        model = Speaker
        fields = '__all__'
