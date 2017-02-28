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
    #url(r'^mo_detail/(?P<pk>[0-9]+)/$', views.mo_detail, name='mo_detail'),
    #url(r'^mo_detail/(?P<location_pk>[0-9]+)/(?P<mo_pk>[0-9]+)/$', views.mo_detail, name='mo_detail'),

    # API views
    url(r'^comp/$', api_views.CompList.as_view()),
    url(r'^comp/(?P<pk>[0-9]+)/$', api_views.CompDetail.as_view()),
    url(r'^mo/$', api_views.MOList.as_view()),
    url(r'^mo/(?P<pk>[0-9]+)/$', api_views.MODetail.as_view()),
    url(r'^api/auditoria/$', api_views.Auditoria.as_view()),
    url(r'^api/auditoria/(?P<pk>[0-9]+)/$', api_views.Auditorias_base.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
