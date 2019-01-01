from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/', include('sponsors.v1.urls'), name='v1_sponsors'),
]
