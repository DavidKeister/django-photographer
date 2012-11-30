from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from feincms.module.page.sitemap import PageSitemap
import markupmirror.urls


admin.autodiscover()
sitemaps = {'pages': PageSitemap}

urlpatterns = patterns('',    
    url(r'^admin/', include(admin.site.urls)),
    (r'^markupmirror/', include(markupmirror.urls.preview)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    (r'^search/', include('haystack.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    url(r'', include('feincms.urls')),
)