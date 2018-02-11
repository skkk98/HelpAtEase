from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from .forms import EventForm
from .models import Event
# Create your views here.
class ngopro(TemplateView):
    template_name = 'ngopro.html'

"""class add_event(View):
    form_class = EventForm
    template_name = 'add_event.html'

    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        image = request.FILES.get('image')

        if form.is_valid():
            title = form.cleaned_data['title']
            place = form.cleaned_data['place']
            description = form.cleaned_data['description']
            contact = form.cleaned_data['contact']
            user_id = request.user
            event = Event(user=user_id, image=image, title=title, description=description, place=place, contact=contact)
            event.save()

            return HttpResponse('your event has been saved')

        return render(request, self.template_name, {'form': form})"""

def add_event(request):
    if request.method == 'GET':
        form = EventForm()
        return render(request, 'add_event.html', {'form': form})
    else:
        title = request.POST['title']
        place = request.POST['place']
        description = request.POST['description']
        contact = request.POST['contact']


        event = Event()
        event.user = request.user
        event.title = title
        event.place = place
        event.description = description
        event.contact = contact


        event.save()
        return HttpResponse('your event has been saved')