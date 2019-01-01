from .serializers import SponsorSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from django.shortcuts import get_object_or_404
from sponsors.forms import SponsorForm
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from user.models import User
from user.v1.serializers import UserSerializer
from django.contrib import messages
from sponsors.models import Sponsor

class SponsorList(APIView):

    def get(self, request):
        sponsors = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def addSponsor(request):
    if request.method == 'POST':
        sponsor_form = SponsorForm(request.POST)
        if sponsor_form.is_valid():
            sponsor_form.save()
            return redirect('sponsor-list')
        else:
            pass

    else:
        sponsor_form = SponsorForm()
        context = {'sponsor_form': sponsor_form}
        return render(request, 'addsponsor.html', context)