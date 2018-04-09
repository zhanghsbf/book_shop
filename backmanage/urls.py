from django.conf.urls import url
from .views import *

urlpatterns = [
   				url(r'^$', manage, name='manager'),
				url(r'^data/$', book_data, name='book_data'),
				url(r'add/category/$', manage_category, name='manage_category'),
				url(r'add/user/$', manage_user, name='manage_user'),
				url(r'add/user/sub/$', manage_user_sub, name='manage_user_sub'),
				url(r'add/user/del/$', manage_user_del, name='manage_user_del'),
			]