from events.models import Event

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from venue.v1.serializers import VenueSerializer
from venue.models import Venue
from venue.forms import VenueForm

class VenueList(APIView):
    """
    List all events, or create a new event.
    """
    def get(self, request, format=None):
        events = Venue.objects.all()
        serializer = VenueSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EventDetail(APIView):
#     """
#     Retrieve, update or delete a event instance.
#     """
#     def get_object(self, pk):
#         return  get_object_or_404(Event.objects.all(), str_id=pk)
#
#
#     def get(self, request, pk, format=None):
#         # try:
#         #     UUID(pk, version=4)
#         #     return super().get(self, request, pk)
#         # except ValueError:
#         #     event = get_object_or_404(Event.objects.all(), str_id=pk)
#         #     return Response(EventSerializer(event).data)
#         event = get_object_or_404(Event.objects.all(), str_id=pk)
#         return Response(EventSerializer(event).data)
#
#     def put(self, request, pk, format=None):
#         event = self.get_object(pk)
#         serializer = EventSerializer(event, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         event = self.get_object(pk)
#         event.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
def addVenue(request):
    if request.method == 'POST':
        venue_form = VenueForm(request.POST)
        if venue_form.is_valid():
            venue_form.save()

            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('venue-list')
        else:
            pass
            # messages.error(request, _('Please correct the error below.'))
    else:
        venue_form = VenueForm()

    return render(request, 'addvenue.html', {
        'venue_form': venue_form
    })
#
# class EventCreate(CreateView):
#     model = Event
#     start_time = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'timepicker'}))
#     # fields = ['name', 'description', 'image_url', 'website_url', 'speaker', 'speaker_image_url', 'speaker_website_url', 'start_time', 'end_time', 'all_day']
#     fields = '__all__'
#
# class EventType(APIView):
#
#     def get(self, request, event_type):
#         print(event_type)
#         events = Event.objects.filter(event_type=event_type)
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data)
#
# class MyEvents(APIView):
#
#     def get(self, request, pk):
#         user = User.objects.get(pk=pk)
#         my_events = user.user_events.all()
#         serializer = EventSerializer(my_events, many=True)
#         return Response(serializer.data)
#
# class Myeventsinuser(APIView):
#
#
#     def post(self, request):
#         user_id = request.data.get('user_id')
#         myevent = request.data.get('event_id')
#         k = str(user_id)
#         print(k)
#         print(str(myevent))
#         user = User.objects.get(user_id=user_id)
#         print(user.user_name)
#         event = Event.objects.get(event_id=myevent)
#         print(event.name)
#         user.user_events.add(event)
#         user.save()
#         print(str(user.user_events))
#         print('Done')
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         print(serializer.data)
#         # return Response({'result':'added'+event.name+'to' + user.user_name}, status.HTTP_200_OK)
#         return Response(serializer.data)
#
