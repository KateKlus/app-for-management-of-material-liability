# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MO(models.Model):
    name = models.CharField("Имя", max_length=200)
    serial = models.CharField("Серия", max_length=200)
    contact = models.CharField("Ответственное лицо", max_length=200)

    class Meta:
        abstract = True

class Tables(MO):
    auditoria = models.CharField("Аудитория", max_length=200)
    location = models.IntegerField()
    class Meta:
        db_table = 'Tables'
        app_label = 'rest_service'

class Location(models.Model):
    name = models.CharField("Аудитория", max_length=200)
    class Meta:
        db_table = 'glpi_locations'
        app_label = 'glpi'

    def __unicode__(self):
        return self.name

class Computer(MO):
    locations = models.ForeignKey(
         Location,
         verbose_name="Аудитория",
         on_delete = models.CASCADE,
    )
    class Meta:
        db_table = 'glpi_computers'
        app_label = 'glpi'

class Monitor(MO):
    locations = models.ForeignKey(
         Location,
         verbose_name="Аудитория",
         on_delete = models.CASCADE,
    )
    class Meta:
        db_table = 'glpi_monitors'
        app_label = 'glpi'