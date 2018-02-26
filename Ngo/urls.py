from django.conf.urls import url
from .views import ngopro, add_event, event_del, event_full, update_event, UpdateEvent
urlpatterns = [
    url(r'^profile/$', ngopro, name='ngopro'),
    url(r'^add/$', add_event, name='addevent'),
    url(r'^(?P<event_id>[0-9]+)/delete/$', event_del, name='event-delete'),
    url(r'^profile/(?P<event_id>[0-9]+)/$', event_full, name='event-full'),
    url(r'^update/(?P<event_id>[0-9]+)/$', update_event, name='event-update'),

]
