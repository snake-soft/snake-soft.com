from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .telegram_bot import Bot


class Home(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        return TemplateView.get(self, request, *args, **kwargs)

    def post(self, request):
        text = request.POST.get('text')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        file = request.POST.get('file')
        bot = Bot()
        bot.send_to_message_system(text, phone, email, file)
        return redirect('home')
