"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import Home, TemplateView
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap


urlpatterns = [
    path('admin/', admin.site.urls),
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
]
