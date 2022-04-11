from django.contrib import admin

from home.forms import ContactUs
from home.models import Contact


class ContactAdmin(admin.ModelAdmin):
    form = ContactUs
    model = Contact
    list_display = ('id', 'name', 'is_processed')
    list_display_links = ('id', 'name', 'is_processed')



admin.site.register(Contact, ContactAdmin)
