from events.models import Event
from .serializers import EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from django.shortcuts import get_object_or_404
from events.forms import EventForm
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from user.models import User
from user.v1.serializers import UserSerializer
from django.contrib import messages

class EventList(APIView):
    """
    List all events, or create a new event.
    """
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    """
    Retrieve, update or delete a event instance.
    """
    def get_object(self, pk):
        return  get_object_or_404(Event.objects.all(), str_id=pk)
        

    def get(self, request, pk, format=None):
        # try:
        #     UUID(pk, version=4)
        #     return super().get(self, request, pk)
        # except ValueError:
        #     event = get_object_or_404(Event.objects.all(), str_id=pk)
        #     return Response(EventSerializer(event).data)
        event = get_object_or_404(Event.objects.all(), str_id=pk)
        return Response(EventSerializer(event).data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)		

def addEvent(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('event-list')
        else:
            pass
            # messages.error(request, _('Please correct the error below.'))
    else:
        event_form = EventForm()
        
    return render(request, 'addevent.html', {
        'event_form': event_form
    })

class EventCreate(CreateView):
    model = Event
    start_time = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    # fields = ['name', 'description', 'image_url', 'website_url', 'speaker', 'speaker_image_url', 'speaker_website_url', 'start_time', 'end_time', 'all_day']
    fields = '__all__'

class EventType(APIView):

    def get(self, request, event_type):
        print(event_type)
        events = Event.objects.filter(event_type=event_type)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class MyEvents(APIView):

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        my_events = user.user_events.all()
        serializer = EventSerializer(my_events, many=True)
        return Response(serializer.data)

class Myeventsinuser(APIView):


    def post(self, request):
        user_id = request.data.get('user_id')
        myevent = request.data.get('event_id')
        k = str(user_id)
        print(k)
        print(str(myevent))
        user = User.objects.get(user_id=user_id)
        print(user.user_name)
        event = Event.objects.get(event_id=myevent)
        print(event.name)
        user.user_events.add(event)
        user.save()
        print(str(user.user_events))
        print('Done')
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        print(serializer.data)
        # return Response({'result':'added'+event.name+'to' + user.user_name}, status.HTTP_200_OK)
        return Response(serializer.data)


def EventChoices(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events/event_choices.html', context)

def Eventupdate(request, event_id):
    instance = get_object_or_404(Event, event_id=event_id)
    event_form = EventForm(request.POST or None, instance=instance)
    print('inside')
    if event_form.is_valid():
        print('inside if')
        instance = event_form.save(commit=False)
        instance.save()
        return redirect('event-list')
    else:
        messages.error(request, 'Please correct the error below.')
        pass
    context = {
        'event_form': event_form
    }
    return render(request, 'addevent.html', context)