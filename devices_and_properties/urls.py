from django.urls import path
from devices_and_properties.views import DevicesView, DevicesChange, PropertiesView, PropertiesChange

urlpatterns = [
    path('devises/', DevicesView.as_view()),
    path('devises/<int:pk>/', DevicesChange.as_view()),
    path('properties/', PropertiesView.as_view()),
    path('devises/<int:pk>/', PropertiesChange.as_view())
]
