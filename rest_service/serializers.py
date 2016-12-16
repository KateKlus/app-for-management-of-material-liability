from rest_framework import serializers
from .models import Tables, Computer

class TablesSerializer(serializers.ModelSerializer):
    label = 'table'
    class Meta:
        model = Tables

        fields = ( 'inv_num', 'type', 'auditoria', 'Contact')

class ComputerSerializer(serializers.ModelSerializer):
    label = 'comp'
    class Meta:
        model = Computer
        fields = ( 'name', 'serial')

class CompTablSerializer(serializers.ModelSerializer):

    table = TablesSerializer(many=True)
    computer = ComputerSerializer(many=True)

