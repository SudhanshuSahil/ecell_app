from events.models import Event
from events.serializers import EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from django.shortcuts import get_object_or_404
from .forms import EventForm
from django.shortcuts import render, redirect

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
		