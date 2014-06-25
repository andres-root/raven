from django.conf.urls import *


urlpatterns = patterns('web.views',
    url(r'^$', 'index', name='index'),
)
