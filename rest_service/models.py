# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Модель материального объекта
class MO(models.Model):
    MO_id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=45)
    serial = models.CharField("Инвентарный номер", max_length=20)
    contact = models.CharField("Ответственное лицо", max_length=45)
    location = models.CharField("Аудитория", max_length=45, default='', blank=True, null=True)
    mo_type = models.CharField("Тип", max_length=45, default='', blank=True, null=True)
    note = models.TextField("Примечание", default='', blank=True, null=True)

    class Meta:
        app_label = 'rest_service'
        db_table = 'MO'
        verbose_name = 'Материальный объект'
        verbose_name_plural = 'Материальные объекты'

    def __unicode__(self):
        return self.name


# Модель аттрибута
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


# Все, что относится к базе GLPI:

# Модель пользователя GLPI
class GLPI_user(models.Model):
    name = models.CharField("Логин", max_length=255)
    realname = models.CharField("Фамилия", max_length=255)
    firstname = models.CharField("Имя", max_length=255)
    user_dn = models.TextField("Информация о пользователе")
    auths_id = models.IntegerField(default=0)

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


# Рекурсивная модель подразделений
class Entities(models.Model):
    name = models.CharField("Название", max_length=255)
    entities_id = models.ForeignKey('self', verbose_name="Родитель", db_column='entities_id')
    level = models.IntegerField()

    class Meta:
        db_table = 'glpi_entities'
        app_label = 'clientapp'
        ordering = ['entities_id_id']

    def __unicode__(self):
        return self.name


# Модель аудитории
class Location(models.Model):
    name = models.CharField("Аудитория", max_length=200)
    entities = models.ForeignKey(
        Entities,
        verbose_name="Подразделение",
        default='Не назначено'
    )
    locations_id = models.IntegerField()

    class Meta:
        db_table = 'glpi_locations'
        app_label = 'clientapp'
        ordering = ['name']
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'

    def __unicode__(self):
        return self.name


# Абстрактный родитель МО
class MO_abstract(models.Model):
    name = models.CharField("Название", max_length=255)
    serial = models.CharField("Серия", max_length=255, default='Не назначено',  blank=True, null=True)
    otherserial = models.CharField("Инвентарный номер", max_length=255, default='Не назначено',  blank=True, null=True)
    entities = models.ForeignKey(
        Entities,
        verbose_name="Подразделение",
    )

    users_id_tech = models.ForeignKey(
        GLPI_user,
        verbose_name="Ответственное лицо",
        db_column='users_id_tech',
        blank=True,
        null=True
    )

    locations = models.ForeignKey(
        Location,
        verbose_name="Аудитория",
    )

    class Meta:
       abstract=True


# Модель компьютера
class Computer(MO_abstract):
    class Meta:
        db_table = 'glpi_computers'
        app_label = 'clientapp'
        ordering = ['name']
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'

    def __unicode__(self):
        return self.name


# Модель монитора
class Monitor(MO_abstract):
    class Meta:
        db_table = 'glpi_monitors'
        app_label = 'clientapp'
        verbose_name = 'Монитор'
        verbose_name_plural = 'Мониторы'

    def __unicode__(self):
        return self.name


# Модель принтера
class Printer(MO_abstract):
    class Meta:
        db_table = 'glpi_printers'
        app_label = 'clientapp'

    def __unicode__(self):
        return self.name


# Модель состоявной части компьютера
class ComputersItems(models.Model):
    items_id = models.IntegerField()
    computers_id = models.ForeignKey(Computer, db_column='computers_id')
    itemtype = models.CharField(max_length=255)

    class Meta:
        db_table = 'glpi_computers_items'
        app_label = 'clientapp'
        ordering = ['computers_id']


# Модель звуковой карты
class DeviceSoundCards(models.Model):
    designation = models.CharField(max_length=255)

    class Meta:
        db_table = 'glpi_devicesoundcards'
        app_label = 'clientapp'

    def __unicode__(self):
        return self.designation


# Модель элемента - звуковой карты
class ItemsDeviceSoundCards(models.Model):
    items_id = models.IntegerField()
    devicesoundcards_id = models.ForeignKey(DeviceSoundCards, db_column='devicesoundcards_id')

    class Meta:
        db_table = 'glpi_items_devicesoundcards'
        app_label = 'clientapp'


# Модель видео карты
class DeviceGraphicCards(models.Model):
    designation = models.CharField(max_length=255)

    class Meta:
        db_table = 'glpi_devicesoundcards'
        app_label = 'clientapp'

    def __unicode__(self):
        return self.designation


# Модель элемента - видео карты
class ItemsDeviceGraphicCards(models.Model):
    items_id = models.IntegerField()
    devicegraphiccards_id = models.ForeignKey(DeviceGraphicCards, db_column='devicegraphiccards_id')

    class Meta:
        db_table = 'glpi_items_devicegraphiccards'
        app_label = 'clientapp'


# Модель памяти
class DeviceMemories(models.Model):
    designation = models.CharField(max_length=255)
    frequence = models.CharField(max_length=255)

    class Meta:
        db_table = 'glpi_devicememories'
        app_label = 'clientapp'

    def __unicode__(self):
        return self.designation


# Модель элемента - памяти
class ItemsDeviceMemories(models.Model):
    items_id = models.IntegerField()
    devicememories_id = models.ForeignKey(DeviceMemories, db_column='devicememories_id')
    size = models.IntegerField()

    class Meta:
        db_table = 'glpi_items_devicememories'
        app_label = 'clientapp'


# Модель жесткого диска
class DeviceHardDrives(models.Model):
    designation = models.CharField(max_length=255)

    class Meta:
        db_table = 'glpi_deviceharddrives'
        app_label = 'clientapp'

    def __unicode__(self):
        return self.designation


# Модель элемента - жесткого лиска
class ItemsDeviceHardDrives(models.Model):
    items_id = models.IntegerField()
    deviceharddrives_id = models.ForeignKey(DeviceHardDrives, db_column='deviceharddrives_id')
    capacity = models.IntegerField()

    class Meta:
        db_table = 'glpi_items_deviceharddrives'
        app_label = 'clientapp'


# Модель процессора
class DeviceProcessors(models.Model):
    designation = models.CharField(max_length=255)
    frequence = models.IntegerField()

    class Meta:
        db_table = 'glpi_deviceprocessors'
        app_label = 'clientapp'

    def __unicode__(self):
        return self.designation


# Модель элемента - процессора
class ItemsDeviceProcessors(models.Model):
    items_id = models.IntegerField()
    deviceprocessors_id = models.ForeignKey(DeviceProcessors, db_column='deviceprocessors_id')
    frequency = models.IntegerField()

    class Meta:
        db_table = 'glpi_items_deviceprocessors'
        app_label = 'clientapp'


# Модель сетевой карты
class DeviceNetworkCards(models.Model):
    designation = models.CharField(max_length=255)

    class Meta:
        db_table = 'glpi_devicenetworkcards'
        app_label = 'clientapp'

    def __unicode__(self):
        return self.designation


# Модель элемента - сетевой карты
class ItemsDeviceNetworkCards(models.Model):
    items_id = models.IntegerField()
    devicenetworkcards_id = models.ForeignKey(DeviceNetworkCards, db_column='devicenetworkcards_id')
    mac = models.CharField(max_length=255)

    class Meta:
        db_table = 'glpi_items_devicenetworkcards'
        app_label = 'clientapp'