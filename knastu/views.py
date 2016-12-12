from django.shortcuts import render
#from .client import RESTClient
#import codecs
#import logging  # @UnresolvedImport
#import unittest  # @UnresolvedImport
from rest_service.views import *
from rest_service.serializers import TablesSerializer
from django.utils.six import BytesIO
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import serializers
import json
#from django.shortcuts import render_to_response

#rc = RESTClient(host='localhost', baseurl='/glpi')
#rc.connect(login_name='glpi', login_password='glpi')

#rc.listObjects(itemtype='computer', rc.get_listObjects(itemtype='computer', start=10, limit=20,)
def main(request):

    request.path = '/rest_service/tables/'
    request.method = 'GET'
    tables = tables_list(request)
    content = tables.data

    #decoded_content = json.loads(content)
    return render(request, 'knastu/tables.html', {'my_tables':content})


def tables(request):

    request.path = '/rest_service/tables/'
    request.method = 'GET'
    tables = tables_list(request)
    content = tables.data

    #decoded_content = json.loads(content)
    return render(request, 'knastu/tables.html', {'my_tables':content})

def table_comp(request):

    request.path = '/rest_service/tables_computers/'
    request.method = 'GET'
    tabl_comp = tables_computers_list(request)
    content = tabl_comp.data

    #decoded_content = json.loads(content)
    return render(request, 'knastu/tables.html', {'tabl_comp':content})

