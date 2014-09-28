from django.conf.urls import patterns, url

from sourdough.base import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='base.index'),
)
