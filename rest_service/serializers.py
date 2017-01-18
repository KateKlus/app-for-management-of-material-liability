from rest_framework import serializers
from .models import *

attr = ['name', 'serial', 'contact']


class TablesSerializer(serializers.ModelSerializer):
    label = 'table'
    class Meta:
        model = Tables
        fields = []
        fields.extend(attr)
        fields.append('auditoria')
        fields.append('location')

class ComputerSerializer(serializers.ModelSerializer):
    label = 'comp'
    class Meta:
        model = Computer
        fields = []
        fields.extend(attr)
        fields.append('locations_id')

class MonitorSerializer(serializers.ModelSerializer):
    label = 'monitor'
    class Meta:
        model = Monitor
        fields = []
        fields.extend(attr)
        fields.append('locations_id')

class LocationSerializer(serializers.ModelSerializer):
    label = 'location'
    class Meta:
        model = Location
        fields = ('name',)

