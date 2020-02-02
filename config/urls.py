# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.urls import path
from home.views import Home, TemplateView, RandomModuleView
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

admin.autodiscover()

urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="base/robots.txt", content_type='text/plain')),
    #path('sitemap.xml', TemplateView.as_view(template_name="base/sitemap.xml", content_type='text/plain')),
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),


    path('cookie/policy/', include('cookie_policy.urls')),
    path('assistant/', RedirectView.as_view(url=reverse_lazy('kontakt')), name='assistant'),
    path('api/django-random/', RandomModuleView, name='assistant'),
]


urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),  # NOQA
    url(r'^', include('cms.urls')),
)


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
