from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
#from polls_cms_integration.models import PollPluginModel
from django.utils.translation import ugettext as _
from .forms import ContactForm

class AssistantPluginPublisher(CMSPluginBase):
    # model = PollPluginModel
    module = _("Assistant")
    name = _("Assistant Plugin")
    render_template = "assistant/assistant.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'form': ContactForm(),
        })
        return context

plugin_pool.register_plugin(AssistantPluginPublisher)