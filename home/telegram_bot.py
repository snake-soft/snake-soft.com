from telegram import Bot as TelegramBotClass


class Bot(TelegramBotClass):
    token = '977467501:AAGrijwmRcxeIRQZos-MKsurZK5LBlK-040'
    message_system_id = -271236783
    
    def __init__(self, *args, **kwargs):
        super().__init__(token=self.token, *args, **kwargs)
    
    def send_to_message_system(self, text, phone, email, file=None):
        message = """
        Neue Anfrage von {} ({}):
        {}
        """.format(email, phone, text)
        return self.send_message(self.message_system_id, message)
