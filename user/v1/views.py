# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.v1.decorators import meta_data_response, session_authorize, catch_exception
from common.v1.utils.error_wrapper import error_wrapper
from . import serializers
from user.models import User
from events.models import Event
from .serializers import UserSerializer
from rest_framework.generics import UpdateAPIView


class UserRegistration(APIView):
    """
    View for the Registration API.
    """
    # @meta_data_response()
    def post(self, request):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            session_data = serializer.save()
            return Response(session_data, status=status.HTTP_200_OK)
        return Response({'error': error_wrapper(serializer.errors)},
                        status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    """
    View for UserLogin
    """
    # @catch_exception()
    # @meta_data_response()
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            session_data = serializer.save()
            return Response(session_data, status=status.HTTP_200_OK)
        print(serializer.errors, 100)
        return Response({'error': error_wrapper(serializer.errors)},
                        status=status.HTTP_401_UNAUTHORIZED)


class UserLogout(APIView):
    """
    View for User Logout
    """
    # @meta_data_response()
    @session_authorize(user_id_key="user_id")
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            serializer = serializers.UserLogoutSerializer(data=request.data)
            serializer.logout_user(
                user_id=auth_data.get('user_id'),
                session_token=auth_data.get('session_token'))
            return Response({}, status.HTTP_200_OK)
        return Response({}, status.HTTP_401_UNAUTHORIZED)

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
