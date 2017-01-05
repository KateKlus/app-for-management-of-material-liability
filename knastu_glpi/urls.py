"""knastu_glpi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import  url, include
from django.contrib import admin
#from rest_service import views
#from knastu import views
admin.autodiscover()

urlpatterns = [
	url(r'^rest_service/', include('rest_service.urls')),
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', views.main, name='main'),
    #url(r'^tables/$', views.tables, name='tables'),
    #url(r'^table_comp/$', views.table_comp, name='table_comp'),
    #url(r'^comp_detail/$', views.comp_detail, name='comp_detail'),
    #url(r'^tables/$', views.tables_list, name='tables_list'),
    #url(r'', include('knastu.urls')),
    
]
