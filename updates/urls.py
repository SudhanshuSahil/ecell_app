from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^api/updates$', views.UpdateList.as_view(), name='update-list'),
    url(r'^updates/add$', views.addUpdate, name='updates-add'),
]
