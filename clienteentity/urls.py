from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clientes/$', views.cliente_list),
    url(r'^clientes/(?P<pk>[0-9]+)/$', views.cliente_detail),
]
