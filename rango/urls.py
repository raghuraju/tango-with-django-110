from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r'^$', views.index, name='rango_index'),
	url(r'about/$', views.about, name='rango_about'),
	url(r'add-category/$', views.add_category, name='rango_add_category'),
	url(r'add-page/(?P<category_slug_url>[\w\-]+)/$', views.add_page, name='rango_add_page'),
	url(r'category/(?P<category_name_url>[\w\-]+)/$', views.show_category, name='rango_show_category'),
]