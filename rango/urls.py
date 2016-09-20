from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r'^$', views.index, name='rango_index'),
	url(r'about/$', views.about, name='rango_about'),
]