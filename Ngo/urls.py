from django.conf.urls import url
from .views import ngopro,add_event,event_del
urlpatterns = [
    url(r'^profile/$',ngopro, name='ngopro'),
    url(r'^add/$', add_event, name='addevent'),
    url(r'^(?P<pk>[0-9]+)/delete/$', event_del, name='event-delete'),

]
