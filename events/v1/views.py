from events.models import Event
from .serializers import EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from django.shortcuts import get_object_or_404
from events.forms import EventForm, EventUpdateForm
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
        myevent_id = request.data.get('event_id')
        k = str(user_id)
        print(k)
        user = User.objects.get(user_id=user_id)
        print(user.user_name)
        event = Event.objects.get(event_id=myevent_id)
        print(event.name)
        try:
            myevent = user.user_events.get(event_id=myevent_id)
            user.user_events.remove(myevent)
            user.save()
            return redirect('my-event', pk=user_id)
            # return Response(status=status.HTTP_204_NO_CONTENT)
        except:

            user.user_events.add(event)
            user.save()
            print(str(user.user_events))
            print('Done')
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            print(serializer.data)
            # return Response({'result':'added'+event.name+'to' + user.user_name}, status.HTTP_200_OK)
            return Response(serializer.data)
            # return Response(status=status.HTTP_204_NO_CONTENT)



def EventChoices(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events/event_choices.html', context)

def Eventupdate(request, event_id):
    instance = get_object_or_404(Event, event_id=event_id)
    event_form = EventUpdateForm(request.POST or None, instance=instance)
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
        'event_form': event_form,
        'event_id': event_id
    }
    return render(request, 'updatevent.html', context)

# class Peoplegoing(APIView):
#
#
#     def post(self, request):
#         event_id = request.data.get('event_id')
#         event = Event.objects.get(event_id=event_id)
#         likes = event.user_set.all().count()
#         return Response({'people_going': likes}, status.HTTP_200_OK)

# class Eventdelete(APIView):
#     def post(self, request):
#         event_id = request.data.get('event_id')
#         user_id = request.data.get('user_id')
#         user = User.objects.get(user_id=user_id)
#         myevent = Event.objects.get(event_id=event_id)
#         user.user_events.remove(myevent)
#         user.save()
#         return redirect('event-list')
class Peoplegoing(APIView):


    def post(self, request):
        # events = Event.objects.all()
        # arr = {'event_id': 'likes'}
        # for event in events:
        #     likes = event.user_set.all().count()
        #     id = str(event.event_id)
        #     likes=str(likes)
        #     arr[id] = likes
        # return Response(arr)
        event_id = request.data.get('event_id')
        event = Event.objects.get(event_id=event_id)
        likes = event.user_set.all().count()
        return Response({'people_going': likes})


def DeleteEvent(request, event_id):
    print('inside delete')
    event = Event.objects.get(event_id=event_id)
    event.delete()
    return redirect('event-list')


