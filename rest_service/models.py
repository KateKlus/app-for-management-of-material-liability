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

    class Meta:
        db_table = 'Tables'
        app_label = 'rest_service'


class Computer(MO):

    class Meta:
        db_table = 'glpi_computers'
        app_label = 'glpi'


