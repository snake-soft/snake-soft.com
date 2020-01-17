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
    path('impressum/', RedirectView.as_view(url='/'), name='impressum'),
    path('datenschutz/', RedirectView.as_view(url='/'), name='datenschutz'),
    path('karriere/', RedirectView.as_view(url='/'), name='karriere'),
    path('ueber-uns/', RedirectView.as_view(url='/'), name='ueberuns'),
    path('kontakt/', RedirectView.as_view(url='/#kontakt'), name='kontakt'),
    path('produkt/webapplikationen/', RedirectView.as_view(url='/'), name='webapplikationen'),
    path('produkt/softwareentwicklung/', RedirectView.as_view(url='/'), name='softwareentwicklung'),
    path('produkt/prozessoptimierung/', RedirectView.as_view(url='/'), name='prozessoptimierung'),
    path('produkt/serververwaltung/', RedirectView.as_view(url='/'), name='serververwaltung'),
    path('technologie/django-webentwicklung/', RedirectView.as_view(url='/'), name='django'),
    path('technologie/python-softwareentwicklung/', RedirectView.as_view(url='/'), name='python'),
    path('technologie/webdesign-webtechnologie/', RedirectView.as_view(url='/'), name='web'),
    
    
    path('robots.txt', TemplateView.as_view(template_name="base/robots.txt", content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name="base/sitemap.xml", content_type='text/plain')),
]
