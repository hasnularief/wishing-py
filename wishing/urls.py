from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import controller

from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
 #	url(r'^admin/', include(admin.site.urls)),
    #path('index/', controller.index),
    #path('', controller.index)
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)