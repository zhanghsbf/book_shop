from django.conf.urls import url
from .views import *

urlpatterns = [
				url(r'^buycar/(?P<post_id>[0-9]+)/$', add_to_buycar, name="add_to_buycar"),
				url(r'^buycar/show/$', show_buycar, name="show_buycar"),
				url(r'^order/add/$', add_order, name="add_order"),
				url(r'^order/user_order/$', user_order, name='user_order'),
				url(r'^order/(?P<order_id>[0-9]+)/$', order, name='order'),
				url(r'^item/confirm/(?P<item_id>[0-9]+)/$', item_confirm, name="item_confirm"),
				url(r'^item/send/(?P<item_id>[0-9]+)/$', item_send, name="item_send"),
				url(r'^item/receive/(?P<item_id>[0-9]+)/$', item_receive, name="item_receive"),
			]