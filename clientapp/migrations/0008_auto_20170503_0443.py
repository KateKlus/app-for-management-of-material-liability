# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-03 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0007_auto_20170418_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputersItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.IntegerField()),
                ('itemtype', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['computers_id'],
                'db_table': 'glpi_computers_items',
            },
        ),
        migrations.CreateModel(
            name='DeviceGraphicCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'glpi_devicesoundcards',
            },
        ),
        migrations.CreateModel(
            name='DeviceHardDrives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'glpi_deviceharddrives',
            },
        ),
        migrations.CreateModel(
            name='DeviceMemories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('frequence', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'glpi_devicememories',
            },
        ),
        migrations.CreateModel(
            name='DeviceNetworkCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('frequence', models.IntegerField()),
            ],
            options={
                'db_table': 'glpi_devicenetworkcards',
            },
        ),
        migrations.CreateModel(
            name='DeviceProcessors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('frequence', models.IntegerField()),
            ],
            options={
                'db_table': 'glpi_deviceprocessors',
            },
        ),
        migrations.CreateModel(
            name='DeviceSoundCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'glpi_devicesoundcards',
            },
        ),
        migrations.CreateModel(
            name='ItemsDeviceGraphicCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.IntegerField()),
                ('devicegraphiccards_id', models.ForeignKey(db_column='devicegraphiccards_id', on_delete=django.db.models.deletion.CASCADE, to='clientapp.DeviceGraphicCards')),
            ],
            options={
                'db_table': 'glpi_items_devicegraphiccards',
            },
        ),
        migrations.CreateModel(
            name='ItemsDeviceHardDrives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('deviceharddrives_id', models.ForeignKey(db_column='deviceharddrives_id', on_delete=django.db.models.deletion.CASCADE, to='clientapp.DeviceHardDrives')),
            ],
            options={
                'db_table': 'glpi_items_deviceharddrives',
            },
        ),
        migrations.CreateModel(
            name='ItemsDeviceMemories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.IntegerField()),
                ('size', models.IntegerField()),
                ('devicememories_id', models.ForeignKey(db_column='devicememories_id', on_delete=django.db.models.deletion.CASCADE, to='clientapp.DeviceMemories')),
            ],
            options={
                'db_table': 'glpi_items_devicememories',
            },
        ),
        migrations.CreateModel(
            name='ItemsDeviceNetworkCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.IntegerField()),
                ('mac', models.CharField(max_length=255)),
                ('devicenetworkcards_id', models.ForeignKey(db_column='devicenetworkcards_id', on_delete=django.db.models.deletion.CASCADE, to='clientapp.DeviceNetworkCards')),
            ],
            options={
                'db_table': 'glpi_items_devicenetworkcards',
            },
        ),
        migrations.CreateModel(
            name='ItemsDeviceProcessors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('deviceprocessors_id', models.ForeignKey(db_column='deviceprocessors_id', on_delete=django.db.models.deletion.CASCADE, to='clientapp.DeviceProcessors')),
            ],
            options={
                'db_table': 'glpi_items_deviceprocessors',
            },
        ),
        migrations.CreateModel(
            name='ItemsDeviceSoundCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.IntegerField()),
                ('devicesoundcards_id', models.ForeignKey(db_column='devicesoundcards_id', on_delete=django.db.models.deletion.CASCADE, to='clientapp.DeviceSoundCards')),
            ],
            options={
                'db_table': 'glpi_items_devicesoundcards',
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('serial', models.CharField(blank=True, default='\u041d\u0435 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043e', max_length=255, null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f')),
                ('otherserial', models.CharField(blank=True, default='\u041d\u0435 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043e', max_length=255, null=True, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('entities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientapp.Entities', verbose_name='\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435')),
                ('locations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientapp.Location', verbose_name='\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f')),
                ('users_id_tech', models.ForeignKey(blank=True, db_column='users_id_tech', null=True, on_delete=django.db.models.deletion.CASCADE, to='clientapp.GLPI_user', verbose_name='\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u043b\u0438\u0446\u043e')),
            ],
            options={
                'db_table': 'glpi_pronters',
            },
        ),
        migrations.AlterField(
            model_name='computer',
            name='entities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientapp.Entities', verbose_name='\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='otherserial',
            field=models.CharField(blank=True, default='\u041d\u0435 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043e', max_length=255, null=True, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='serial',
            field=models.CharField(blank=True, default='\u041d\u0435 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043e', max_length=255, null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='users_id_tech',
            field=models.ForeignKey(blank=True, db_column='users_id_tech', null=True, on_delete=django.db.models.deletion.CASCADE, to='clientapp.GLPI_user', verbose_name='\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u043b\u0438\u0446\u043e'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='entities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientapp.Entities', verbose_name='\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='otherserial',
            field=models.CharField(blank=True, default='\u041d\u0435 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043e', max_length=255, null=True, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='serial',
            field=models.CharField(blank=True, default='\u041d\u0435 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043e', max_length=255, null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='users_id_tech',
            field=models.ForeignKey(blank=True, db_column='users_id_tech', null=True, on_delete=django.db.models.deletion.CASCADE, to='clientapp.GLPI_user', verbose_name='\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u043b\u0438\u0446\u043e'),
        ),
        migrations.AddField(
            model_name='computersitems',
            name='computers_id',
            field=models.ForeignKey(db_column='computers_id', on_delete=django.db.models.deletion.CASCADE, to='clientapp.Computer'),
        ),
    ]