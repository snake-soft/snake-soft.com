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
from home.views import Home
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('impressum/', Home.as_view(), name='impressum'),
    path('datenschutz/', Home.as_view(), name='datenschutz'),
    path('karriere/', Home.as_view(), name='karriere'),
    path('ueber-uns/', Home.as_view(), name='ueberuns'),
    path('kontakt/', RedirectView.as_view(url='/#kontakt'), name='kontakt'),
    path('produkt/webapplikationen/', Home.as_view(), name='webapplikationen'),
    path('produkt/softwareentwicklung/', Home.as_view(), name='softwareentwicklung'),
    path('produkt/prozessoptimierung/', Home.as_view(), name='prozessoptimierung'),
    path('produkt/serververwaltung/', Home.as_view(), name='serververwaltung'),
    path('technologie/django-webentwicklung/', Home.as_view(), name='django'),
    path('technologie/python-softwareentwicklung/', Home.as_view(), name='python'),
    path('technologie/webdesign-webtechnologie/', Home.as_view(), name='web'),
]
