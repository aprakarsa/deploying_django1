from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^update/(?P<pk>[0-9]+)$', views.update, name='update'),
	url(r'^delete/(?P<pk>[0-9]+)$', views.delete, name='delete'),
	url(r'^create/$', views.create, name='create'),
	url(r'^$', views.list, name='list'),
]

