from django.db import models


class Devices(models.Model):
    name = models.CharField(max_length=200)


class Properties(models.Model):
    properties = models.ManyToManyField("Devices", related_name="properties")
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
