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
from home.views import Home, TemplateView
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
    
    path('', Home.as_view(), name='home'),
    path('impressum/', TemplateView.as_view(template_name="content/impressum.html"), name='impressum'),
    path('datenschutz/', TemplateView.as_view(template_name="content/datenschutz.html"), name='datenschutz'),
    path('karriere/', TemplateView.as_view(template_name="content/karriere.html"), name='karriere'),
    path('ueber-uns/', TemplateView.as_view(template_name="content/ueber-uns.html"), name='ueberuns'),
    path('kontakt/', TemplateView.as_view(template_name="content/kontakt_entry.html"), name='kontakt'),
    path('software-webdesign-wordpress-philosophie/', TemplateView.as_view(template_name="content/philosophie.html"), name='philosophie'),

    path('produkt/webapplikationen/', TemplateView.as_view(template_name="produkt/webapplikationen.html"), name='webapplikationen'),
    path('produkt/softwareentwicklung/', TemplateView.as_view(template_name="produkt/softwareentwicklung.html"), name='softwareentwicklung'),
    path('produkt/prozessoptimierung/', TemplateView.as_view(template_name="produkt/prozessoptimierung.html"), name='prozessoptimierung'),
    path('produkt/serververwaltung/', TemplateView.as_view(template_name="produkt/serververwaltung.html"), name='serververwaltung'),
    path('technologie/django-webentwicklung/', TemplateView.as_view(template_name="technologie/django.html"), name='django'),
    path('technologie/python-softwareentwicklung/', TemplateView.as_view(template_name="technologie/python.html"), name='python'),
    path('technologie/webdesign-webtechnologie/', TemplateView.as_view(template_name="technologie/web.html"), name='web'),

    path('robots.txt', TemplateView.as_view(template_name="base/robots.txt", content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name="base/sitemap.xml", content_type='text/plain')),

    path('cookie/policy/', include('cookie_policy.urls')),
    path('assistant/', RedirectView.as_view(url=reverse_lazy('kontakt')), name='assistant'),

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
