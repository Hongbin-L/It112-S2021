from django.contrib import admin
from .models import Meeting, Minute, Resource, Event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Minute)
admin.site.register(Resource)
admin.site.register(Event)