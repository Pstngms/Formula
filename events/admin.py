from .models import Events, EventsRegistration
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class EventsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), label='Описание')

    class Meta:
        model = Events
        fields = '__all__'


class EventsAdmin(admin.ModelAdmin):
    form = EventsAdminForm
    list_display = ('id', 'title', 'is_published', 'start_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class EventsRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'user_email', 'is_registered', 'created')
    list_filter = ('event', 'user_email')


admin.site.register(Events, EventsAdmin)
admin.site.register(EventsRegistration, EventsRegistrationAdmin)
