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


class MOList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = Tables.objects.all()
    serializer_class = TablesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MODetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

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

