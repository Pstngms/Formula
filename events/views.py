from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from accounts.models import CustomUser
from events.models import Events, EventsRegistration
from news.models import News


def events_page(request):
    events = Events.objects.all()
    return render(request, 'events/events.html', {'events': events})


class ViewEvents(DetailView):
    model = Events


class AddReg(View):
    def post(self, request, *args, **kwargs):
        events_post_id = int(request.POST.get('events_post_id'))
        user_id = int(request.POST.get('user_id'))
        url_form = request.POST.get('url_form')

        user_inst = CustomUser.objects.get(id=user_id)
        events_post_inst = Events.objects.get(id=events_post_id)

        try:
            events_post_inst = EventsRegistration.objects.get(event=events_post_inst, user_email=user_inst)
        except Exception as e:
            event_post = EventsRegistration(event=events_post_inst, user_email=user_inst, is_registered=True)
            event_post.save()
        return redirect(url_form)


class RemoveReg(View):
    def post(self, request, *args, **kwargs):
        events_reg_id = int(request.POST.get('events_reg_id'))
        url_form = request.POST.get('url_form')
        event_post = EventsRegistration.objects.get(id=events_reg_id)
        event_post.delete()
        return redirect(url_form)
