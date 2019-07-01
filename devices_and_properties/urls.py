from django.urls import path

from devices_and_properties.views import DevicesView, DevicesChange, PropertiesView, PropertiesChange, DevicesProperties

urlpatterns = [
    path('devices/', DevicesView.as_view()),
    path('devices/<int:pk>/', DevicesChange.as_view()),
    path('properties/', PropertiesView.as_view()),
    path('devices/<int:pk>/', PropertiesChange.as_view()),
    path('devices/<int:pk>/properties', DevicesProperties.as_view())
]
