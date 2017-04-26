from rest_framework import serializers
from .models import *

attr = ['name', 'serial', 'otherserial', 'users_id_tech']


class MOSerializer(serializers.ModelSerializer):
    label = 'MO'

    class Meta:
        model = MO
        fields = ('MO_id', 'name',  'serial', 'contact', 'location', 'mo_type', 'note')


class AttributeSerializer(serializers.ModelSerializer):
    label = 'Attribute'

    class Meta:
        model = Attribute
        fields = ('attr_name',  'attr_value', 'MO')


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
        fields = ('id', 'name', 'entities_id', 'locations_id',)


class GLPI_userSerializer(serializers.ModelSerializer):
    label = 'GLPI_user'

    class Meta:
        model = GLPI_user
        fields = ('id', 'name', 'realname', 'firstname', 'user_dn')
