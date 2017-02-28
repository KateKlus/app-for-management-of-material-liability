# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#абстрактный родитель МО
class MO_abstract(models.Model):
    name = models.CharField("Название", max_length=45)
    serial = models.CharField("Инвентарный номер", max_length=30)
    contact = models.CharField("Ответственное лицо", max_length=45)

    class Meta:
       abstract = True


#модель материального объекта
class MO(models.Model):
    mo_id = models.IntegerField(primary_key=True)
    name = models.CharField("Название", max_length=45)
    serial = models.CharField("Инвентарный номер", max_length=20)
    contact = models.CharField("Ответственное лицо", max_length=45)
    location = models.CharField("Аудитория", max_length=45)
    type = models.CharField("Тип", max_length=45)

    class Meta:
        db_table = 'MO'
        app_label = 'rest_service'

#модель аттрибута
class Attribute(models.Model):
    attribute_id = models.IntegerField(primary_key=True)
    attr_name = models.CharField("Аттрибут", max_length=45)
    attr_value = models.CharField("Значение", max_length=45)
    mo = models.ForeignKey(
        MO,
        verbose_name="МО",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'Attribute'
        app_label = 'rest_service'

#описание моделей БД GLPI
class Location(models.Model):
    name = models.CharField("Аудитория", max_length=200)
    entities_id = models.IntegerField()
    locations_id = models.IntegerField()
    class Meta:
        db_table = 'glpi_locations'
        app_label = 'glpi'

    def __unicode__(self):
        return self.name

class Computer(MO_abstract):
    locations = models.ForeignKey(
         Location,
         verbose_name="Аудитория",
         on_delete = models.CASCADE,
    )
    class Meta:
        db_table = 'glpi_computers'
        app_label = 'glpi'

class Monitor(MO_abstract):
    locations = models.ForeignKey(
         Location,
         verbose_name="Аудитория",
         on_delete = models.CASCADE,
    )
    class Meta:
        db_table = 'glpi_monitors'
        app_label = 'glpi'

