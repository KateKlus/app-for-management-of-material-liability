# -*- coding: utf-8 -*-
from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static
from . import views, api_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # Session Login
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    # Regular Django Views
    url(r'^$', views.index, name='index'),
    url(r'^auditorias/$', views.auditorias.as_view(), name='auditorias'),  # список аудиторий
    url(r'^auditorias/get_mo_list/(?P<pk>[0-9]+)/$', views.auditorias_base, name='auditorias_base'),  # оборудование по аудиториям
    url(r'^entities/$', views.entities.as_view(), name='entities'),  # архитектура подразделений
    url(r'^entities/get_mo_list/(?P<pk>[0-9]+)/$', views.entities_base, name='entities_base'),  # архитектура подразделений

    # получить список ответственных специалистов
    url(r'^responsible_specialist/$', views.responsible_specialist.as_view(), name='responsible_specialist'),
    # получить подотчетное оборудование по id специалиста
    url(r'^responsible_specialist/get_mo_list/(?P<pk>[0-9]+)/$', views.specialist_mo_list, name='specialist_mo_list'),
    # Получить детальную информацию о компьютере
    url(r'^get_comp_detail_info/(?P<pk>[0-9]+)/$', views.comp_detail_info, name='comp_detail_info'),

    # получить подотчетное оборудование по id пользователя
    url(r'^responsible_specialist_mo_list/$', views.specialist_mo_list_userid, name='user_specialist_mo_list'),
    url(r'^responsible_specialist_mo_list/get_mo_detail/(?P<pk>[0-9]+)/$', views.get_mo_detail, name='get_mo_detail'),
    url(r'^responsible_specialist_mo_list/get_comp_detail/(?P<pk>[0-9]+)/$', views.get_comp_detail, name='get_comp_detail'),
    url(r'^responsible_specialist_mo_list/get_monitor_detail/(?P<pk>[0-9]+)/$', views.get_monitor_detail, name='get_comp_detail'),

    # Удаление объектов
    url(r'^del_comp/(?P<pk>[0-9]+)$', views.computersDelete.as_view(), name='del_comp'),
    url(r'^del_monitor/(?P<pk>[0-9]+)$', views.monitorsDelete.as_view(), name='del_monitor'),
    url(r'^del_mo/(?P<pk>[0-9]+)$', views.moDelete.as_view(), name='del_mo'),
    url(r'^del_attr/(?P<pk>[0-9]+)$', views.attrDelete.as_view(), name='del_attr'),

    # Обновление объектов
    url(r'^update_comp/(?P<pk>[0-9]+)$', views.computersUpdate.as_view(), name='update_comp'),
    url(r'^update_monitor/(?P<pk>[0-9]+)$', views.monitorsUpdate.as_view(), name='update_monitor'),
    url(r'^update_mo/(?P<pk>[0-9]+)$', views.moUpdate.as_view(), name='update_mo'),
    url(r'^update_attr/(?P<pk>[0-9]+)$', views.attrUpdate.as_view(), name='update_attr'),

    #Создание объектов
    url(r'^create_mo/$', views.mobjCreate.as_view(), name='create_mo'),
    url(r'^create_mo/create_attribute/$', views.attrCreate.as_view(), name='create_attribute'),

    # Перенос группы оборудования
    url(r'^responsible_specialist_mo_list/mo_transfer/json/$', views.transfer, name='transfer_json'),
    url(r'^responsible_specialist_mo_list/mo_transfer/json/(?P<loc>\w+)/(?P<mo_list>\w+)$', views.transfer, name='transfer_json_with_key'),

    # API views
    url(r'^api/comp/$', api_views.CompList.as_view()),
    url(r'^api/comp/(?P<pk>[0-9]+)/$', api_views.CompDetail.as_view()),
    url(r'^api/mo/$', api_views.MOList.as_view()),
    url(r'^api/mo/(?P<pk>[0-9]+)/$', api_views.MODetail.as_view()),
    url(r'^api/auditoria/$', api_views.Auditoria.as_view()),
    url(r'^api/auditoria/(?P<pk>[0-9]+)/$', api_views.Auditorias_base.as_view()),
    url(r'^api/specialist_moList/(?P<pk>[0-9]+)/$', api_views.Specialist_moList.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
