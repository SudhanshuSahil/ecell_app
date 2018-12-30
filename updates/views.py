from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Update
from updates.serializers import UpdateSerializer
from updates.forms import UpdateForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


class UpdateList(APIView):
    """
        List all events, or create a new event.
        """
    def get(self, request, format=None):
        updates = Update.objects.all()
        serializer = UpdateSerializer(updates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def addUpdate(request):
    if request.method == 'POST':
        update_form = UpdateForm(data=request.POST)
        if update_form.is_valid():
            update_form.save()

            return redirect('update-list')
        else:
            pass
    else:
        update_form = UpdateForm()
    context = {'update_form': update_form}
    return render(request,'addupdate.html',context)