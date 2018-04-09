from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^profile/(?P<user_id>[0-9]+)/$', profile, name="profile"),
	url(r'^login/', login, name='login'),
	url(r'^logout/', logout, name='logout'),
]