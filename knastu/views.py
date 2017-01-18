# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import *
import urllib2
import json

#from .client import RESTClient
#import codecs
#import logging  # @UnresolvedImport
#import unittest  # @UnresolvedImport
from rest_service.views import *
from django.shortcuts import redirect

from django.utils.six import BytesIO
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import serializers

#from django.shortcuts import render_to_response

#rc = RESTClient(host='localhost', baseurl='/glpi')
#rc.connect(login_name='glpi', login_password='glpi')

#rc.listObjects(itemtype='computer', rc.get_listObjects(itemtype='computer', start=10, limit=20,)

def main(request):

    return render(request, 'knastu/tables.html')


def tables(request):

    request.path = '/rest_service/mo/'
    request.method = 'GET'
    tables = MOList().get()

    #content = tables.data

    #decoded_content = json.loads(content)
    return render(request, 'knastu/tables.html', {'my_tables':    tables.data})

def table_comp(request):
    if request.method == "GET":
        form = LocationForm(request.GET)
        if form.is_valid():
            request.path = '/rest_service/Auditorias_base/'
            request.method = 'GET'
            content = Auditorias_base.get(form.data)
            return render(request, 'knastu/auditorias_base.html', {'base': content})
    else:
        form = LocationForm()
    return render(request, 'knastu/auditorias_base.html', {'form': form})

def comp_detail(request):

    if request.method == "GET":
        form = LocationForm(request.GET)
        if form.is_valid():

            request.path = '/rest_service/Auditorias_base/'
            request.method = 'GET'
            content = Auditorias_base(form.f).get()
            return render(request, 'knastu/auditorias_base.html', {'base': content})
    else:
        form = LocationForm()
    return render(request, 'knastu/auditorias_base.html', {'form':form})

#Добавление компьютера через форму
def add_comp(request):
    if request.method == "POST":
        form = ComputerForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.save()
            #return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = ComputerForm()
    return render(request, 'knastu/add_comp.html', {'form': form})

#
def responsible_person(request):
    if request.method == "POST":
        form = ComputerForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.save()
            #return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = ComputerForm()
    return render(request, 'knastu/add_comp.html', {'form': form})