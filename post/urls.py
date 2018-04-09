from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^write/', write, name='write'),
	url(r'^post/(?P<post_id>[0-9]+)/$', posts, name='post'),
	url(r'^userpost/(?P<user_id>[0-9]+)/$', user_post, name='user_post'),
	url(r'^usercomment/(?P<user_id>[0-9]+)/$', user_comment, name='user_comment'),
	url(r'category/(?P<cate_id>[0-9]+)/$', category, name='category'),
]

