from django.conf.urls import url
from .views import ngopro,add_event
urlpatterns = [
    url(r'^profile/$',ngopro.as_view(), name='ngopro'),
    url(r'^add/$', add_event, name='addevent'),

]
