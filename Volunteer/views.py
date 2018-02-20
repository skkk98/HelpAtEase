from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View
from Ngo.models import Event
from .models import Regevent
# Create your views here.
"""class profile(TemplateView):
    template_name = 'profile.html'"""


def profile(request):
    all_events = Event.objects.all()
    template_name = 'profile.html'
    return render(request, template_name, {'all_events': all_events})

def event_reg(request, event_id):
    user_id = request.user
    if Regevent.objects.filter(user=user_id).exists():
        finduser = Regevent.objects.get(user=user_id)
        finduser.events += str(event_id) + '&'
        finduser.save()
    else:
        regevent = Regevent(user=user_id, events=str(event_id) + '&')
        regevent.save()
    return HttpResponseRedirect('/volunteer/profile')

def regd_events(request):
    template_name = 'regd_events.html'
    user_id = request.user
    find_events = Regevent.objects.get(user=user_id)
    list_events = find_events.events.split('&')
    print(list_events)
    list_events = list_events[:-1]
    events = Event.objects.filter(id__in=list_events)
    return render(request, template_name, {'events': events})
