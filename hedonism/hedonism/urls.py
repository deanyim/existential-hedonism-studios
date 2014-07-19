from django.conf.urls import include, patterns, url

import website.urls


urlpatterns = patterns(
    '',
    url(r'^$', include(website.urls)),
)
