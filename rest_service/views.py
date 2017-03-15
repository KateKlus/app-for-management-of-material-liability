# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Attribute as AttributeModel
from api_views import *

from django.shortcuts import redirect
from django.conf import settings

from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.urls import reverse_lazy

def index(request):
    if not request.user.is_authenticated():
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    template_name = 'knastu/index.html'
    return render(request, template_name)

#для вывода списка аудиторий из базы glpi
class auditorias(generic.ListView):
    model = Location
    template_name = 'knastu/auditorias.html'


#для вывода списка оборудования из обеих баз
def auditorias_base(request, pk):
    if not request.user.is_authenticated():
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    location = Location.objects.get(pk=pk)
    comps = Computer.objects.filter(locations=pk)
    monitors = Monitor.objects.filter(locations=pk)
    mo_list = MO.objects.filter(location=location.name)

    mo_attr_dict = []

    for mo in mo_list:
        attr = AttributeModel.objects.filter(MO=mo.MO_id)
        mo_attr_dict.append(attr)

    return render(request, 'knastu/auditorias_base.html', {
        'comps': comps,
        'monitors': monitors,
        'mo_list':mo_list,
        'mo_attr_dict': mo_attr_dict,
    })

#для удаления объектов
class computersDelete(generic.DeleteView):
    model = Computer
    success_url = reverse_lazy('auditorias')

class monitorsDelete(generic.DeleteView):
    model = Monitor
    success_url = reverse_lazy('auditorias')

class moDelete(generic.DeleteView):
    model = MO
    success_url = reverse_lazy('auditorias')

class attrDelete(generic.DeleteView):
    model = AttributeModel
    success_url = reverse_lazy('auditorias')

#для редактирования объектов
class computersUpdate(generic.UpdateView):
    model = Computer
    fields = ['name', 'serial', 'contact', 'locations']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('auditorias')

class monitorsUpdate(generic.UpdateView):
    model = Monitor
    fields = ['name', 'serial', 'contact', 'locations', 'type']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('auditorias')

class moUpdate(generic.UpdateView):
    model = MO
    fields = ['name', 'serial', 'contact', 'location', 'mo_type']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('auditorias')

class attrUpdate(generic.UpdateView):
    model = AttributeModel
    fields = ['attr_name', 'attr_value']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('auditorias')

#для добавления объектов
class computersCreate(generic.CreateView):
    model = Computer
    fields = ['name', 'serial', 'contact', 'locations']
    template_name_suffix = '_create_form'
    success_url = "/"

class monitorsCreate(generic.CreateView):
    model = Monitor
    fields = ['name', 'serial', 'contact', 'locations']
    template_name_suffix = '_create_form'
    success_url = "/"

class mobjCreate(generic.CreateView):
    model = MO
    fields = ['name',  'serial', 'contact', 'location', 'mo_type']
    template_name_suffix = '_create_form'
    success_url = "create_attribute"

class attrCreate(generic.CreateView):
    model = AttributeModel
    fields = ['attr_name',  'attr_value', 'MO']
    template_name_suffix = '_create_form'
    success_url = "/"

#вход
class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "knastu/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
#выход
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")