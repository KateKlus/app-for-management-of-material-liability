from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tables(models.Model):
    #idTables = models.IntegerField()
	inv_num = models.IntegerField()
	type = models.TextField()
	auditoria = models.TextField()
	Contact = models.TextField()

	class Meta:
		db_table = 'Tables'
		app_label = 'rest_service'
        name = 'table'

class Location(models.Model):
	name = models.CharField(max_length=7)

	class Meta:
		db_table = 'glpi_locations'
		app_label = 'glpi'

class Computer(models.Model):
	name = models.TextField()
	serial = models.TextField()
	#location = models.ForeignKey(Location)

	class Meta:
		db_table = 'glpi_computers'
		app_label = 'glpi'

