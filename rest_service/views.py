from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

from itertools import chain

from .models import *
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

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Auditorias_base(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Computer.objects.all()
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comps = Computer.objects.filter(locations__name = pk)
        serializer = ComputerSerializer(comps, many=True)

        my_tables = Tables.objects.filter(location = pk)
        serializer1 = TablesSerializer(my_tables, many=True)
        content = serializer.data + serializer1.data

        return Response(content)
'''
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


'''

@api_view(['GET', 'POST'])
def tables_list(request):
    if request.method == 'GET':
        my_tables = Tables.objects.all()
        serializer = TablesSerializer(my_tables, many=True)

        content = serializer.data
        json = JSONRenderer().render(content)
        return Response(content)

    elif request.method == 'POST':
        serializer = TablesSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])

def tables_computers_list(request):
    if request.method == 'GET':
        my_computers = Computer.objects.all()
        my_tables = Tables.objects.all()

        serializer = ComputerSerializer(my_computers, many=True)
        serializer1 = TablesSerializer(my_tables, many=True)

        content = serializer.data + serializer1.data


        json = JSONRenderer().render(content)
        return Response(content)
'''

