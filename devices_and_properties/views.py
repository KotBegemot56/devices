from rest_framework import generics

from devices_and_properties.models import Devices, Properties
from devices_and_properties.serializers import DevicesSerializer, PropertiesSerializer


class DevicesView(generics.ListCreateAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


class DevicesChange(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


class PropertiesView(generics.ListCreateAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer


class PropertiesChange(generics.RetrieveUpdateDestroyAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer
