from django.shortcuts import render
from django.views.generic import TemplateView, View
from Ngo.models import Event
# Create your views here.
"""class profile(TemplateView):
    template_name = 'profile.html'"""


def profile(request):
    all_events = Event.objects.all()
    template_name = 'profile.html'
    return render(request, template_name, {'all_events': all_events})
