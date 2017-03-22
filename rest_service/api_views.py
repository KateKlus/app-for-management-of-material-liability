from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_service.models import Attribute as AttributeModel
from rest_service.serializers import *

import json


class MOList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = MO.objects.all()
    serializer_class = MOSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MODetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = MO.objects.all()
    serializer_class = MOSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#computers
class CompList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CompDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#auditorias

class Auditoria(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Auditorias_base(APIView):
    def get_object(self, pk):
        try:
            return Computer.objects.all()
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comps = Computer.objects.filter(locations__id = pk)
        serializer = ComputerSerializer(comps, many=True)

        monitors = Monitor.objects.filter(locations__id=pk)
        serializer2 = MonitorSerializer(monitors, many=True)

        location = Location.objects.get(pk=pk)

        mo = MO.objects.filter(location=location.name)
        serializer1 = MOSerializer(mo, many=True)

        content = serializer.data + serializer1.data + serializer2.data

        return Response(content)

    def get_auditorium(self):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        content = serializer.data
        return Response(content)

class Specialist_moList(APIView):
    def get(self, request, pk, format=None):
        specialist = GLPI_user.objects.get(pk=pk)
        specialist_ser = GLPI_userSerializer(specialist)
        comps = Computer.objects.filter(users_id_tech_id=pk)
        comps_ser = ComputerSerializer(comps, many=True)
        monitors = Monitor.objects.filter(users_id_tech_id=pk)
        monitors_ser = MonitorSerializer(monitors, many=True)
        mo_list = MO.objects.filter(contact=specialist.name)
        mo_ser = MOSerializer(mo_list, many=True)

        mo_attr_dict =[]

        for mo in mo_list:
            attr = AttributeModel.objects.filter(MO=mo.MO_id)
            attr_ser = AttributeSerializer(attr, many=True)
            mo_attr_dict.append({mo.MO_id : attr_ser.data})

        return Response({
            'specialist': specialist_ser.data,
            'comps': comps_ser.data,
            'monitors': monitors_ser.data,
            'mo_list': mo_ser.data,
            'mo_attr_dict': mo_attr_dict,
        })


    def get_auditorium(self):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        content = serializer.data
        return Response(content)