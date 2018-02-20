from django.conf.urls import url
from . import views
from .views import profile, event_reg, regd_events

urlpatterns = [
    url(r'^profile/$', profile, name='profile'),
    url(r'^(?P<event_id>[0-9]+)/regevent$', event_reg, name='event-register'),
    url(r'^profile/regevents$', regd_events, name='registered-events')

]
