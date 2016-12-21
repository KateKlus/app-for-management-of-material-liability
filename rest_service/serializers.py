from rest_framework import serializers
from .models import *

attr = ['name', 'serial', 'contact']

class MOSerializer(serializers.ModelSerializer):
    class Meta:
        model = MO
        fields = '__all__'
        #abstract = True

class TablesSerializer(serializers.ModelSerializer):
    label = 'table'
    class Meta:
        model = Tables
        fields = attr
        #fields.append('auditoria')


class ComputerSerializer(serializers.ModelSerializer):
    label = 'comp'
    class Meta:
        model = Computer
        fields = attr

class CompTablSerializer(serializers.ModelSerializer):

    table = TablesSerializer(many=True)
    computer = ComputerSerializer(many=True)

