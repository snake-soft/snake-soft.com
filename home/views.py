from django.shortcuts import render
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'home/home.html'
    
    #===========================================================================
    # def get(self, request, *args, **kwargs):
    #     response = TemplateView.get(self, request, *args, **kwargs)
    #     from django.contrib import messages
    #     messages.add_message(request, messages.INFO, 'Hello world.')
    #     return response
    #===========================================================================
