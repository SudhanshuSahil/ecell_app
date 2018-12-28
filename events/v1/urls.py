from django.conf.urls import url
from django.urls import path,  include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([


    # url(r'^chat/public-room/', include(django_eventstream.urls)
    # , {'channels': ['public-room']}),

    # url(r'^chat/(?P<chat_id1>[0-9]+)/(?P<chat_id2>[0-9]+)/',include(django_eventstream.urls)
    # , {'format-channels': ['{chat_id1}-{chat_id2}']}),

    # url(r'^chat/online-users/', include(django_eventstream.urls)
    # , {'channels': ['online-users']}),
    path('api/events/myevent_add', views.Myeventsinuser.as_view(), name='v1_myevent_add'),
	path('api/events/<event_type>', views.EventType.as_view(), name='event-type'),
	path('api/events/myevents/<pk>', views.MyEvents.as_view(), name='my-event'),
	path('api/events', views.EventList.as_view(), name = 'event-list'),
    path('api/events/<pk>', views.EventDetail.as_view(), name='event-detail'),
	# path('events/add', views.EventCreate.as_view(), name='event-add'),
	path('events/add', views.addEvent, name='event-add'),
	path('events/update/<event_id>', views.Eventupdate, name='event-update'),
	path('events/choices', views.EventChoices, name='event-choices')

    # url(r'^chat/api/(?P<chat_id1>[0-9]+)/(?P<chat_id2>[0-9]+)/message/$',
    #     views.Private_room_message.as_view(),
    #     name='private_message'),

    # url(r'^chat/api/rooms/(?P<room_url>[^/]+)/messages/$',
    #     views.RoomMessageList.as_view(),
    #     name='room_message-list'),

    # url(r'^chat/api/pri_rooms/(?P<chat_id1>[0-9]+)/(?P<chat_id2>[0-9]+)/messages/$',
    #     views.PriRoomMessageList.as_view(),
    #     name='priroom_message-list'),

    # url(r'^chat/api/pri_rooms/(?P<chat_id1>[0-9]+)/(?P<chat_id2>[0-9]+)/$',
    #     views.PriRoomDetail.as_view(),
    #     name='priroom_detail'),

    # url(r'^chat/api/is_blockedby/(?P<chat_id1>[0-9]+)/(?P<chat_id2>[0-9]+)/$',
    #     views.Check_blocked.as_view(),
    #     name='check-blocked'),

    # url(r'^chat/api/users/block/$',
    #     views.UserBlock.as_view(),
    #     name='block-user'),

    # url(r'^chat/api/users/(?P<chat_id>[0-9]+)/is_mod/$',
    #     views.Is_mod.as_view(),
    #     name='is_mod'),


    # url(r'^chat/api/users/(?P<chat_id>[0-9]+)/$',
    #     views.User_Detail.as_view(),
    #     name='user_detail'),

    # url(r'^chat/api/users/(?P<chat_id>[0-9]+)/full/$',
    #     views.User_ChatDetail.as_view(),
    #     name='user_chat_detail'),

    # url(r'^chat/api/contact_list/(?P<chat_id>[0-9]+)/$',
    #     views.ContactList.as_view(),
    #     name='contact-list'),

    # url(r'^chat/api/online_users/$',
    #     views.onlineUsers.as_view(),
    #     name='online-users'),

    # url(r'^chat/zeus/v1/admin/user/(?P<chat_id>[0-9]+)/chat_role/$',
    #     views.EditChatRole.as_view(),
    #     name='edit-chat-role'),

])
