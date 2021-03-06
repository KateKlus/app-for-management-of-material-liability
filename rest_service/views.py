# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.db.models import Count
from django.shortcuts import redirect, render
from django.conf import settings
from api_views import *
from django.http import JsonResponse
from itertools import chain
from collections import OrderedDict
from forms import *
import json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    if not request.user.is_authenticated():
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    template_name = 'knastu/index.html'
    return render(request, template_name)


# для вывода списка аудиторий из базы glpi
class auditorias(generic.ListView):
    model = Location
    template_name = 'knastu/auditorias.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(auditorias, self).dispatch(request, *args, **kwargs)


# для вывода списка аудиторий из базы glpi
class entities(generic.ListView):
    model = Entities
    template_name = 'knastu/entities.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(entities, self).dispatch(request, *args, **kwargs)


# для вывода списка ответственных из базы glpi
class responsible_specialist(generic.ListView):
    model = GLPI_user
    template_name = 'knastu/responsible_person.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(responsible_specialist, self).dispatch(request, *args, **kwargs)


# для вывода списка оборудования из обеих баз по id аудитории
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
        'user': request.user,
        'location': location.name,
    })


# для вывода списка оборудования из обеих баз по подразделениям
def entities_base(request, pk):
    if not request.user.is_authenticated():
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    comps = Computer.objects.filter(entities_id=pk)
    monitors = Monitor.objects.filter(entities_id=pk)
    #mo_list = MO.objects.filter(location=loc.name)

    #mo_attr_dict = []

    #for mo in mo_list:
    #    attr = AttributeModel.objects.filter(MO=mo.MO_id)
    #    mo_attr_dict.append(attr)

    return render(request, 'knastu/entities_base.html', {
        'comps': comps,
        'monitors': monitors,
        #'mo_list':mo_list,
        #'mo_attr_dict': mo_attr_dict,
        'user': request.user,
        #'location': location.name,
    })


# для вывода списка оборудования из обеих баз по id специалиста
def specialist_mo_list(request, pk):
    if not request.user.is_authenticated():
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    specialist = GLPI_user.objects.get(pk=pk)
    specialist_fullname = specialist.user_dn.split(',')[0]
    comps = Computer.objects.filter(users_id_tech_id=pk)
    monitors = Monitor.objects.filter(users_id_tech_id=pk)
    mo_list = MO.objects.filter(specialist__specialist_name=specialist)

    mo_attr_dict = []

    for mo in mo_list:
        attr = AttributeModel.objects.filter(MO=mo.MO_id)
        mo_attr_dict.append(attr)

    return render(request, 'knastu/responsible_spec_moList.html', {
        'spec_name': specialist_fullname[3:],
        'comps': comps,
        'monitors': monitors,
        'mo_list':mo_list,
        'mo_attr_dict': mo_attr_dict,
        'user': request.user,
    })


# Для вывода списка оборудования из обеих баз по id пользователя
def specialist_mo_list_userid(request):
    if not request.user.is_authenticated():
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    # Получаем имя и фамилию пользователя
    real_name = request.user.last_name
    second_name = request.user.first_name

    # Находим ответственного
    specialist = GLPI_user.objects.get(realname=real_name, firstname=second_name)

    # Получаем его полное имя и id
    specialist_fullname = specialist.user_dn.split(',')[0]
    spec_id = specialist.id

    # Получаем технику и МО специалиста
    comps = Computer.objects.filter(users_id_tech_id=spec_id)
    monitors = Monitor.objects.filter(users_id_tech_id=spec_id)
    mo_list = MO.objects.filter(specialist__specialist_name=specialist)

    # Определяем какие типы МО имеются
    types = mo_list.values('mo_type').annotate(count=Count('name')).order_by('mo_type')
    types_list = types.values_list('mo_type', 'count')

    # Создаем словарь {тип_мо: список_мо}
    types_of_mo_dict = {}
    for type in types:
        type_name = type.values()
        mo_by_types_list = mo_list.filter(mo_type=type_name[0])
        types_of_mo_dict.update({type_name[0]: mo_by_types_list.values('MO_id', 'name', 'serial', 'location', 'note',
                                                                       'mo_type')})

    # Определяем какие аудитории имеются
    locations = mo_list.values('location').annotate(count=Count('name')).order_by('location')
    glpi_comps_locations = comps.values('locations__name').annotate(count=Count('name')).order_by('locations__name')
    glpi_monitors_locations = monitors.values('locations__name').annotate(count=Count('name')).order_by('locations__name')

    # Создаем словарь {аудитория: список_мо}
    locations_of_mo_dict = {}

    # Добавляем некомпьютерное оборудование
    for loc in locations:
        location = loc.values()
        mo_by_location_list = mo_list.filter(location=location[1])
        locations_of_mo_dict.update({location[1]: mo_by_location_list.values('MO_id', 'name', 'serial', 'location',
                                                                             'note', 'mo_type')})

    # Добавляем компьютеры
    for loc in glpi_comps_locations:
        location = loc.values()
        mo_by_location_list = comps.filter(locations__name=location[1])

        if locations_of_mo_dict.get(location[1]):
            value = list(chain(mo_by_location_list.values('name', 'otherserial', 'users_id_tech__name',
                                                          'locations__name', ), locations_of_mo_dict.get(location[1])))
            locations_of_mo_dict.update({location[1]: value})
        else:
            locations_of_mo_dict.update({location[1]: mo_by_location_list.values('name', 'otherserial',
                                                                                 'users_id_tech__name', 'locations__name' )})

    # Добавляем мониторы
    for loc in glpi_monitors_locations:
        location = loc.values()
        mo_by_location_list = monitors.filter(locations__name=location[1])

        if locations_of_mo_dict.get(location[1]):
            value = list(chain(mo_by_location_list.values('name', 'otherserial', 'users_id_tech__name',
                                                          'locations__name', ), locations_of_mo_dict.get(location[1])))
            locations_of_mo_dict.update({location[1]: value})
        else:
            locations_of_mo_dict.update({location[1]: mo_by_location_list.values('name', 'otherserial',
                                                                                 'users_id_tech__name', 'locations__name' )})

    # Сортируем словарь по ключам
    ord_dict = OrderedDict()
    for k in sorted(locations_of_mo_dict.keys()):
        ord_dict[k] = locations_of_mo_dict[k]


    return render(request, 'knastu/responsible_user_moList.html', {
        'user': request.user,
        'spec_name': specialist_fullname[3:],

        'comps': comps,
        'monitors': monitors,
        'mo_list':mo_list,

        'types': types_list,
        'mo_dict': types_of_mo_dict,

        'mo_dict_loc': ord_dict,

    })


# Получение детальной информации о компонентах компьютера
def comp_detail_info(request, pk):
    comp = Computer.objects.get(pk=pk)
    printers = ComputersItems.objects.filter(computers_id=pk, itemtype='Printer')
    monitors = ComputersItems.objects.filter(computers_id=pk, itemtype='Monitor')
    peripherals = ComputersItems.objects.filter(computers_id=pk, itemtype='Peripheral')

    printers_list = []
    monitors_list = []

    for printer in printers:
        printers_list.append(Printer.objects.get(pk=printer.items_id))

    for monitor in monitors:
        monitors_list.append(Monitor.objects.get(pk=monitor.items_id))

    if peripherals:
        for peripheral in peripherals:
            network_cards = ItemsDeviceNetworkCards.objects.filter(items_id=peripheral.items_id)
            processors = ItemsDeviceProcessors.objects.filter(items_id=peripheral.items_id)
            hard_drives = ItemsDeviceHardDrives.objects.filter(items_id=peripheral.items_id)
            memories = ItemsDeviceMemories.objects.filter(items_id=peripheral.items_id)
            graphic_cards = ItemsDeviceGraphicCards.objects.filter(items_id=peripheral.items_id)
            sound_cards = ItemsDeviceSoundCards.objects.filter(items_id=peripheral.items_id)
    else:
        network_cards = []
        processors = []
        hard_drives = []
        memories = []
        graphic_cards = []
        sound_cards = []


    return render(request, 'knastu/comp_detail_info.html', {
        'NetworkCards': network_cards,
        'Processors': processors,
        'HardDrives': hard_drives,
        'Memories': memories,
        'GraphicCards': graphic_cards,
        'SoundCards': sound_cards,
        'Printers': printers_list,
        'Monitors': monitors_list,
        'Comp': comp,
    })


def get_comp_detail(request, pk):
    if not request.user.is_authenticated():
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    comp = Computer.objects.get(id=pk)

    return render(request, 'knastu/glpi_detail_result.html', {
        'mo': comp,
    })


def get_monitor_detail(request, pk):
    if not request.user.is_authenticated():
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    monitor = Monitor.objects.get(id=pk)

    return render(request, 'knastu/glpi_detail_result.html', {
        'mo': monitor,
    })


def get_mo_detail(request, pk):
    if not request.user.is_authenticated():
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    mo_attr_dict = []
    attr = AttributeModel.objects.filter(MO=pk)
    mo_attr_dict.append(attr)

    return render(request, 'knastu/mo_detail_result.html', {
        'mo_attr_dict': mo_attr_dict,
    })


# RUD компьютеры
class computersUpdate(generic.UpdateView):
    model = Computer
    form_class = ComputerUpdateForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('auditorias')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(computersUpdate, self).dispatch(request, *args, **kwargs)


class computersDelete(generic.DeleteView):
    model = Computer
    success_url = reverse_lazy('auditorias')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(computersDelete, self).dispatch(request, *args, **kwargs)


# CRUD мониторы
class monitorsUpdate(generic.UpdateView):
    model = Monitor
    form_class = MonitorUpdateForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('auditorias')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(monitorsUpdate, self).dispatch(request, *args, **kwargs)


class monitorsDelete(generic.DeleteView):
    model = Monitor
    success_url = reverse_lazy('auditorias')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(monitorsDelete, self).dispatch(request, *args, **kwargs)


# CRUD материальные объекты и аттрибуты
class mobjCreate(generic.CreateView):
    model = MO
    fields = ['name',  'serial', 'location', 'mo_type', 'note', 'specialist',]
    template_name_suffix = '_create_form'
    success_url = "create_attribute"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(mobjCreate, self).dispatch(request, *args, **kwargs)


class attrCreate(generic.CreateView):
    model = AttributeModel
    fields = ['attr_name',  'attr_value', 'MO']
    template_name_suffix = '_create_form'
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(attrCreate, self).dispatch(request, *args, **kwargs)


class moUpdate(generic.UpdateView):
    model = MO
    fields = ['name', 'serial', 'location', 'mo_type', 'note', 'specialist',]
    template_name_suffix = '_update_form'
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(moUpdate, self).dispatch(request, *args, **kwargs)


class attrUpdate(generic.UpdateView):
    model = AttributeModel
    fields = ['attr_name', 'attr_value']
    template_name_suffix = '_update_form'
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(attrUpdate, self).dispatch(request, *args, **kwargs)


class moDelete(generic.DeleteView):
    model = MO
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(moDelete, self).dispatch(request, *args, **kwargs)


class attrDelete(generic.DeleteView):
    model = AttributeModel
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(attrDelete, self).dispatch(request, *args, **kwargs)


def transfer(request, loc=None, mo_list=None,):
    loc = request.GET.get('loc')
    mo_list = json.loads(request.GET.get('mo_list'))

    # Выбираются все записи из таблици Location с указанным именем, упорядоченные по уровню вложенности
    # подразделений и берется ПОСЛЕДНЯЯ запись. В эту аудиторию будет перенесено оборудование.
    try:
        location = Location.objects.filter(name=loc).order_by('-entities__level')[0]
    except Location.DoesNotExist:
        return JsonResponse({'Error': 'Location does not exist'})

    comps = []
    monitors = []
    other = []

    for mo in mo_list:
        mo_type_id = mo.split(' ')
        if mo_type_id[0] == u'comp':
            comps.append(int(mo_type_id[1]))
        if mo_type_id[0] == u'monitor':
            monitors.append(int(mo_type_id[1]))
        if mo_type_id[0] == u'mo':
            other.append(int(mo_type_id[1]))

    if other:
        for mo in other:
            mo_obj = MO.objects.get(MO_id=mo)
            mo_obj.location = loc
            mo_obj.save()

    if comps or monitors:
        for comp in comps:
            comp_obj = Computer.objects.get(id=comp)
            comp_obj.locations = location
            comp_obj.save()

        for monitor in monitors:
            monitor_obj = Monitor.objects.get(id=monitor)
            monitor_obj.locations = location
            monitor_obj.save()

    return JsonResponse({'Success': 'OK'})


# вход
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "knastu/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


# выход
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
