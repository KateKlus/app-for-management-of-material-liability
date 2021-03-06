# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-21 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('serial', models.CharField(max_length=30, verbose_name='\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
            ],
            options={
                'db_table': 'glpi_computers',
            },
        ),
        migrations.CreateModel(
            name='GLPI_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u041b\u043e\u0433\u0438\u043d')),
                ('realname', models.CharField(max_length=255, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('firstname', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
                ('user_dn', models.TextField(verbose_name='\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435')),
            ],
            options={
                'ordering': ['realname'],
                'db_table': 'glpi_users',
                'verbose_name': '\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442',
                'verbose_name_plural': '\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f')),
                ('entities_id', models.IntegerField()),
                ('locations_id', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'glpi_locations',
            },
        ),
        migrations.AddField(
            model_name='computer',
            name='locations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientapp.Location', verbose_name='\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='computer',
            name='users_id_tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientapp.GLPI_user', verbose_name='\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u043b\u0438\u0446\u043e'),
        ),
    ]
