from django.conf.urls import url, include
from . import views

#from rest_framework import routers
#from rest_service import views

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^tables/$', views.tables, name='tables'),
    url(r'^table_comp/$', views.table_comp, name='table_comp'),
    url(r'^comp_detail/$', views.comp_detail, name='comp_detail'),
    url(r'^add_comp/$', views.add_comp, name='add_comp'),
    url(r'^responsible_person/$', views.responsible_person, name='responsible_person'),

    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]