from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static
from . import views, api_views
from rest_framework.authtoken import views as rest_framework_views


urlpatterns = [
    # Session Login
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),

    # Regular Django Views
    url(r'^$', views.index, name='index'),
    url(r'^auditorias/$', views.auditorias.as_view(), name='auditorias'),
    url(r'^auditorias/get_mo_list/(?P<pk>[0-9]+)/$', views.auditorias_base, name='auditorias_base'),

    url(r'^del_comp/(?P<pk>[0-9]+)$', views.computersDelete.as_view(), name='del_comp'),
    url(r'^del_monitor/(?P<pk>[0-9]+)$', views.monitorsDelete.as_view(), name='del_monitor'),
    url(r'^del_mo/(?P<pk>[0-9]+)$', views.moDelete.as_view(), name='del_mo'),
    url(r'^del_attr/(?P<pk>[0-9]+)$', views.attrDelete.as_view(), name='del_attr'),

    url(r'^update_comp/(?P<pk>[0-9]+)$', views.computersUpdate.as_view(), name='update_comp'),
    url(r'^update_monitor/(?P<pk>[0-9]+)$', views.monitorsUpdate.as_view(), name='update_monitor'),
    url(r'^update_mo/(?P<pk>[0-9]+)$', views.moUpdate.as_view(), name='update_mo'),
    url(r'^update_attr/(?P<pk>[0-9]+)$', views.attrUpdate.as_view(), name='update_attr'),

    url(r'^create_comp/$', views.computersCreate.as_view(), name='create_comp'),
    url(r'^create_monitor/$', views.monitorsCreate.as_view(), name='create_monitor'),
    url(r'^create_mo/$', views.mobjCreate.as_view(), name='create_mo'),
    url(r'^create_mo/create_attribute/$', views.attrCreate.as_view(), name='create_attribute'),

    #url(r'^mo_detail/(?P<pk>[0-9]+)/$', views.mo_detail, name='mo_detail'),
    #url(r'^mo_detail/(?P<location_pk>[0-9]+)/(?P<mo_pk>[0-9]+)/$', views.mo_detail, name='mo_detail'),

    # API views
    url(r'^api/comp/$', api_views.CompList.as_view()),
    url(r'^api/comp/(?P<pk>[0-9]+)/$', api_views.CompDetail.as_view()),
    url(r'^api/mo/$', api_views.MOList.as_view()),
    url(r'^api/mo/(?P<pk>[0-9]+)/$', api_views.MODetail.as_view()),
    url(r'^api/auditoria/$', api_views.Auditoria.as_view()),
    url(r'^api/auditoria/(?P<pk>[0-9]+)/$', api_views.Auditorias_base.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
