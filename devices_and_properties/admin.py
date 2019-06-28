from django.contrib import admin

from devices_and_properties.models import Devices, Properties

admin.site.register(Devices)
admin.site.register(Properties)