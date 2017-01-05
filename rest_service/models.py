from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MO(models.Model):
    name = models.TextField()
    serial = models.TextField()
    contact = models.TextField()

    class Meta:
        abstract = True

class Tables(MO):
    auditoria = models.TextField()
    location = models.IntegerField()
    class Meta:
        db_table = 'Tables'
        app_label = 'rest_service'

class Location(models.Model):
    name = models.TextField()
    class Meta:
        db_table = 'glpi_locations'
        app_label = 'glpi'

class Computer(MO):
    locations = models.ForeignKey(
         Location,
         on_delete = models.CASCADE,
    )
    class Meta:
        db_table = 'glpi_computers'
        app_label = 'glpi'

