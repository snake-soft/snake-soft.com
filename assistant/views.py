from .forms import ContactForm
from django.views.generic.edit import FormView
from home.telegram_bot import Bot
from django.contrib import messages
from django.shortcuts import redirect


class Assistant(FormView):
    template_name = 'assistant/assistant.html'
    form_class = ContactForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return redirect('/#assistant')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        data = form.cleaned_data
        message = data.get('message', '')
        phone = data.get('phone', '')
        email = data.get('email', '')
        file = data.get('file', None)

        bot = Bot()
        bot.send_to_message_system(message, phone, email, file)
        messages.add_message(
            self.request,
            messages.INFO,
            'Ihre Anfrage wurde übersandt.\nWir werden sie schnellstmöglich beantworten.'
            )
        return super().form_valid(form)
