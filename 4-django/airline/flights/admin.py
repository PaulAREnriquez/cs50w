from django.contrib import admin

from .models import Flight, Airport, Passenger


# A custom setting for our admin flights page
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

# A custom setting for our admin passenger page
class PasengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",) # a tuple
# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PasengerAdmin)
