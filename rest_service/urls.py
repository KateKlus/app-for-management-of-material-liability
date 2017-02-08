from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static
from . import views, api_views

urlpatterns = [
    # Regular Django Views
    url(r'^$', views.index, name='index'),

    # API views
    url(r'^comp/$', api_views.CompList.as_view()),
    url(r'^comp/(?P<pk>[0-9]+)/$', api_views.CompDetail.as_view()),
    url(r'^mo/$', api_views.MOList.as_view()),
    url(r'^mo/(?P<pk>[0-9]+)/$', api_views.MODetail.as_view()),
    #url(r'^auditoria/$', api_views.Auditoria.as_view()),
    #url(r'^auditoria/(?P<pk>[0-9]+)/$', api_views.Auditorias_base.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
