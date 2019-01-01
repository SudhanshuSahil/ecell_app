from .serializers import SpeakerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from django.shortcuts import get_object_or_404
from speakers.forms import SpeakerForm
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from user.models import User
from user.v1.serializers import UserSerializer
from django.contrib import messages
from speakers.models import Speaker

class SpeakerList(APIView):

    def get(self, request):
        speakers = Speaker.objects.all()
        serializer = SpeakerSerializer(speakers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpeakerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def addSpeaker(request):
    if request.method == 'POST':
        speaker_form = SpeakerForm(request.POST)
        if speaker_form.is_valid():
            speaker_form.save()
            return redirect('speaker-list')
        else:
            pass

    else:
        speaker_form = SpeakerForm()
        context = {'speaker_form': speaker_form}
        return render(request, 'addspeaker.html', context)