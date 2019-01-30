from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Chat
from django import forms
from friends.models import Friend

class ChatForm(forms.ModelForm, ):
    # start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    # # date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    from_friend = forms.ModelChoiceField(queryset=Friend.objects.all(), widget=forms.Select, empty_label=None)
    # to_friend = forms.ModelChoiceField(queryset=Friend.objects.all(), widget=forms.Select, empty_label=None)
    class Meta:
        model = Chat
        fields = '__all__'

# class EventsChoices(forms.ModelForm):
#     events = forms.ModelChoiceField(queryset=Event.objects.all(), widget=forms.Select, empty_label=None)
#     class Meta:
#         fields = 'events'
# class EventUpdateForm(forms.ModelForm):
#     start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
#     # date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
#     venue = forms.ModelChoiceField(queryset=Venue.objects.all(), widget=forms.Select, empty_label=None)
#     class Meta:
#         model = Event
#         fields = '__all__'

