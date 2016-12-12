from django.conf.urls import  url
from rest_service import views

urlpatterns = [
    url(r'^tables/$', views.tables_list, name='tables_list'),
    url(r'^computers/$', views.computers_list, name='computers_list'),
    url(r'^tables_computers/$', views.tables_computers_list, name='tables_computers_list'),
    #url(r'', include('knastu.urls')),
    
]
