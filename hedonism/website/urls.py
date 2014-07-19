from django.conf.urls import patterns, url

from website.views import views


urlpatterns = patterns(
    '', url(r'^$', views.index, name='index')
)
