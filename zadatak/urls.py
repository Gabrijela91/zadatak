from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns ('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^assignment/', include('assignment.urls')),
	url(r'^$', 'index'),
	url(r'^$', 'zadatak'),
    
    
    
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



