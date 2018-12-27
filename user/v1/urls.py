from django.conf.urls import url

from user.v1 import views

urlpatterns = [
    # url(r'^user/myevent_add$', views.Myeventsinuser.as_view(), name='v1_myevent_add'),
    url(r'^api/user/userlist$', views.UserListall.as_view(), name='users-api'),
    url(r'^user/register/', views.UserRegistration.as_view(),
        name='v1_UserRegistration'),
    url(r'^user/login/', views.UserLogin.as_view(), name='v1_UserLogin'),
    url(r'^user/logout/$', views.UserLogout.as_view(), name='v1_UserLogout'),

]
