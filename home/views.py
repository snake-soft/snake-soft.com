from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    
    #===========================================================================
    # def get(self, request, *args, **kwargs):
    #     response = TemplateView.get(self, request, *args, **kwargs)
    #     from django.contrib import messages
    #     messages.add_message(request, messages.INFO, 'Hello world.')
    #     return response
    #===========================================================================
