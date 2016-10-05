from django.conf.urls import url
from rango import views

app_name = 'rango'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'about/$', views.about, name='about'),
	url(r'register/$', views.register, name='register'),
	url(r'login/$', views.user_login, name='login'),
	url(r'logout/$', views.user_logout, name='logout'),
	url(r'restricted/$', views.restricted, name='restricted'),
	url(r'add-category/$', views.add_category, name='add_category'),
	url(r'add-page/(?P<category_slug_url>[\w\-]+)/$', views.add_page, name='add_page'),
	url(r'category/(?P<category_name_url>[\w\-]+)/$', views.show_category, name='show_category'),
]