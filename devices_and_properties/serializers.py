from rest_framework import serializers

from devices_and_properties.models import Devices, Properties


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'


class DevicesPropertiesSerializer(serializers.ModelSerializer):
    properties = PropertiesSerializer(many=True)

    class Meta:
        model = Devices
        fields = "__all__"
