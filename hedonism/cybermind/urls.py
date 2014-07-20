from django.conf.urls import patterns, url

from cybermind.views import views


urlpatterns = patterns(
    '',
    url(r'^(?P<name>[a-zA-Z]*)/$', views.cybermind, name='cybermind')
)
