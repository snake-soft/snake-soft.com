from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .forms import PassgenForm
from .generator import Generator, CharSet
from django.http import JsonResponse

@plugin_pool.register_plugin
class PassgenPlugin(CMSPluginBase):
    model = CMSPlugin
    module = _("Passgen")
    name = _("Password Generator Plugin")
    render_template = "passgen/passgen_form.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(PassgenPlugin, self).render(context, instance, placeholder)
        request = context['request']

        if request.method == 'GET':
            form = PassgenForm(request.session)

        elif request.method == 'POST':
            form = PassgenForm(request.POST)
            if form.is_valid():
                for name, obj in form.fields.items():
                    if name not in ['output']:
                        request.session[name] = form.cleaned_data[name]

        context['passgen_form'] = form
        context['generated_password'] = self.generate_password(request)
        return context

    def generate_password(self, request):
        charsets = []
        if 'length' in request.session:
            length = request.session['length']
        else:
            length = 16
        for name, enabled in request.session.items():
            if enabled:
                charsets.append(name)
        charsets = CharSet.by_name(*charsets)
        return Generator(charsets).get_password(length=length)
