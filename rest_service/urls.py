from django.conf.urls import  url
from rest_service import views

urlpatterns = [
    #url(r'^tables/$', views.tables_list, name='tables_list'),
    #url(r'^tables_computers/$', views.tables_computers_list, name='tables_computers_list'),

    #class based
    url(r'^mo/$', views.MOList.as_view()),
    url(r'^mo/(?P<pk>[0-9]+)/$', views.MODetail.as_view()),

    url(r'^comp/$', views.CompList.as_view()),
    url(r'^comp/(?P<pk>[0-9]+)/$', views.CompDetail.as_view()),
    url(r'^auditoria/$', views.Auditoria.as_view()),

    url(r'^auditoria/(?P<pk>[0-9]+)/$', views.Auditorias_base.as_view()),
    #url(r'', include('knastu.urls')),
    
]
