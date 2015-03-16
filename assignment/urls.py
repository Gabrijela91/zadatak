from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns ('',
    url(r'^$', views.index, name='index'),
	url(r'^$', views.zadatak, name='zadatak'),
    url(r'url2$', views.url2, name='url2'),
	url(r'url3$', views.url3, name='url3'),


	#url(r'^$', 'app.main.index', name='root'),
	#url(r'^index$', 'app.main.index', name='index'),
	#url(r'^index.html$', 'app.main.index', name='index'),
)


                        




