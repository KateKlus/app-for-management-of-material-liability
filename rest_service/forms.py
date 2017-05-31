# -*- coding: utf-8 -*-
from django import forms
from models import Location, Monitor, Computer


class MonitorUpdateForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ['name', 'serial', 'otherserial', 'users_id_tech', 'locations']

    locations = forms.ModelChoiceField(queryset=Location.objects.none(), label="Аудитория")

    def __init__(self, *args, **kwargs):
        super(MonitorUpdateForm, self).__init__(*args, **kwargs)
        self.fields['locations'].queryset = Location.objects.filter(level=2).order_by('-entities__level').distinct().order_by('name')


class ComputerUpdateForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['name', 'serial', 'otherserial', 'users_id_tech', 'locations']

    locations = forms.ModelChoiceField(queryset=Location.objects.none(), label="Аудитория")

    def __init__(self, *args, **kwargs):
        super(ComputerUpdateForm, self).__init__(*args, **kwargs)
        self.fields['locations'].queryset = Location.objects.filter(level=2).exclude(entities_id = 0).order_by('-entities__level').distinct().order_by('name')