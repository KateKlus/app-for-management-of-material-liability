from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_service.serializers import *


class MOList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Tables.objects.all()
    serializer_class = TablesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MODetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = Tables.objects.all()
    serializer_class = TablesSerializer
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
        comps = Computer.objects.filter(locations__name = pk)
        serializer = ComputerSerializer(comps, many=True)

        tables = Tables.objects.filter(location = pk)
        serializer1 = TablesSerializer(tables, many=True)

        monitors = Monitor.objects.filter(locations__name=pk)
        serializer2 = MonitorSerializer(monitors, many=True)
        content = serializer.data + serializer1.data + serializer2.data

        return Response(content)

    def get_auditorium(self):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        content = serializer.data
        return Response(content)