from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import *
from rest_service.serializers import *


@api_view(['GET', 'POST'])
def tables_list(request):
    """
    List all tables, or create a new task.
    """
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
def computers_list(request):
    """
    List all tables, or create a new task.
    """
    if request.method == 'GET':
        my_computers = Computer.objects.all()
        serializer = ComputerSerializer(my_computers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ComputerSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])

def tables_computers_list(request):
    """
    List all tables, or create a new task.
    """
    if request.method == 'GET':
        my_computers = Computer.objects.all()
        my_tables = Tables.objects.all()

        serializer = CompTablSerializer(my_tables, my_computers, many=True)
        content = serializer.data
        json = JSONRenderer().render(content)
        return Response(content)

    
