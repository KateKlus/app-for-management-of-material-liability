# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#модель материального объекта
class MO(models.Model):
    MO_id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=45)
    serial = models.CharField("Инвентарный номер", max_length=20)
    contact = models.CharField("Ответственное лицо", max_length=45)
    location = models.CharField("Аудитория", max_length=45)
    mo_type = models.CharField("Тип", max_length=45)

    class Meta:
        app_label = 'rest_service'
        db_table = 'MO'
        verbose_name = 'Материальный объект'
        verbose_name_plural = 'Материальные объекты'

    def __unicode__(self):
        return self.name

#модель аттрибута
class Attribute(models.Model):
    Attribute_id = models.AutoField(primary_key=True)
    attr_name = models.CharField("Аттрибут", max_length=45)
    attr_value = models.CharField("Значение", max_length=45)
    MO = models.ForeignKey(
        MO,
        verbose_name="МО",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'Attribute'
        app_label = 'rest_service'
        verbose_name = 'Аттрибут'
        verbose_name_plural = 'Аттрибуты'

    def __unicode__(self):
        return self.attr_name


#модель пользователя GLPI
class GLPI_user(models.Model):
    name = models.CharField("Логин", max_length=255)
    realname = models.CharField("Фамилия", max_length=255)
    firstname = models.CharField("Имя", max_length=255)
    user_dn = models.TextField("Информация о пользователе")
    auths_id = models.IntegerField( default=0)

    class Meta:
        db_table = 'glpi_users'
        app_label = 'clientapp'
        verbose_name = 'Ответственный специалист'
        verbose_name_plural = 'Ответственные специалисты'
        ordering = ['realname']

    def __unicode__(self):
        user_data = unicode(self.user_dn).split(',')[0]
        if user_data == 'None':
            return self.name
        else:
            return user_data[3:]

# рекурсивная модель подразделений
class Entities(models.Model):
    name = models.CharField("Название", max_length=255)
    entities_id = models.ForeignKey('self', verbose_name="Родитель", db_column = 'entities_id')
    level = models.IntegerField()

    class Meta:
        db_table = 'glpi_entities'
        app_label = 'clientapp'
        ordering = ['entities_id_id']

    def __unicode__(self):
        return self.name

# описание моделей БД GLPI
class Location(models.Model):
    name = models.CharField("Аудитория", max_length=200)
    entities = models.ForeignKey(
        Entities,
        verbose_name="Подразделение",
    )
    locations_id = models.IntegerField()

    class Meta:
        db_table = 'glpi_locations'
        app_label = 'clientapp'
        ordering = ['name']

    def __unicode__(self):
        return self.name

#абстрактный родитель МО
class MO_abstract(models.Model):
    name = models.CharField("Название", max_length=255)
    serial = models.CharField("Серия", max_length=255, default='Не назначено')
    otherserial = models.CharField("Инвентарный номер", max_length=255, default='Не назначено')
    entities = models.ForeignKey(
        Entities,
        verbose_name="Подразделение",
    )

    users_id_tech = models.ForeignKey(
        GLPI_user,
        verbose_name="Ответственное лицо",
        db_column = 'users_id_tech'
    )

    locations = models.ForeignKey(
        Location,
        verbose_name="Аудитория",
        on_delete=models.CASCADE,
    )

    class Meta:
       abstract = True


#модель компьютера
class Computer(MO_abstract):
    class Meta:
        db_table = 'glpi_computers'
        app_label = 'clientapp'
        ordering = ['name']

    def __unicode__(self):
        return self.name

#модель монитора
class Monitor(MO_abstract):

    class Meta:
        db_table = 'glpi_monitors'
        app_label = 'clientapp'

