"""
Password Length:
Include Symbols: ( e.g. @#$% )
Include Numbers: ( e.g. 123456 )
Include Lowercase Characters: ( e.g. abcdefgh )
Include Uppercase Characters: ( e.g. ABCDEFGH )
Exclude Similar Characters: ( e.g. i, l, 1, L, o, 0, O )
Exclude Ambiguous Characters: ( { } [ ] ( ) / \ ' " ` ~ , ; : . < > )
#Generate On Your Device: ( do NOT send across the Internet )
#Auto-Select: ( select the password automatically )
#Save My Preference: ( save all the settings above for later use )
#Load My Settings Anywhere: URL to load my settings on other computers quickly

Buttons:
- Generate Password
- Copy Result

Input:
- disabled password output
"""
from django import forms
from django.utils.translation import ugettext_lazy as _

class BooleanField(forms.BooleanField):
    def __init__(self, *args, **kwargs):
        if not 'initial' in kwargs:
            kwargs['initial'] = True
        if not 'required' in kwargs:
            kwargs['required'] = False
        super().__init__(*args, **kwargs)
        self.widget.attrs['onchange'] = 'this.form.submit()'

class OutputField(forms.CharField):
    def __init__(self, *args, **kwargs):
        if not 'required' in kwargs:
            kwargs['required'] = False
        kwargs['initial'] = 'fdsaf'
        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        return forms.CharField.prepare_value(self, value)

class SliderField(forms.IntegerField):
    def __init__(self, *args, **kwargs):
        if not 'min_value' in kwargs:
            kwargs['min_value'] = 0
        if not 'max_value' in kwargs:
            kwargs['max_value'] = 100
        if not 'initial' in kwargs:
            kwargs['initial'] = 16
        super().__init__(*args, **kwargs)
        self.widget.attrs['onchange'] = 'this.form.submit()'


class PassgenForm(forms.Form):
    length = SliderField(label=_('length'), required=False)

    symbols = BooleanField(label=_('Include Symbols'))
    numbers = BooleanField(label=_('Include Numbers'))
    lowercase = BooleanField(label=_('Include Lowercase Characters'))
    uppercase = BooleanField(label=_('Include Uppercase Characters'))
    ambiguous = BooleanField(label=_('Include Ambiguous Characters'))

    #    def __init__(self, *self, ):

    #===========================================================================
    # def get_initial_for_field(self, field, field_name):
    #     print(field_name, forms.Form.get_initial_for_field(self, field, field_name))
    #     if field_name == 'output':
    #         import pdb; pdb.set_trace()  # <---------
    #         return 'bla'
    #     return forms.Form.get_initial_for_field(self, field, field_name)
    #===========================================================================
