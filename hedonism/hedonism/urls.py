from django.conf.urls import include, patterns, url

import cybermind.urls
import website.urls


urlpatterns = patterns(
    '',
    url(r'^$', include(website.urls)),
    url(r'^cybermind/', include(cybermind.urls))
)
