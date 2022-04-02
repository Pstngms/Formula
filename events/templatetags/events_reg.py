from django import template

from events.models import EventsRegistration

register = template.Library()


@register.simple_tag(takes_context=True)
def is_reg(context, event_id):
    request = context['request']
    try:
        event_post = EventsRegistration.objects.get(event_id=event_id,
                                                    user_email=request.user.id).is_registered
    except Exception as e:
        event_post = False

    print(event_post)
    return event_post


@register.simple_tag(takes_context=True)
def events_r_id(context, event_id):
    request = context['request']
    return EventsRegistration.objects.get(event_id=event_id, user_email=request.user.id).id
