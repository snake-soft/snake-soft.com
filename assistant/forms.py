from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label='E-Mail')
    phone = forms.CharField(required=False, label='Tel')
    message = forms.CharField(widget=forms.Textarea, label='Anfrage')
    file = forms.FileField(required=False, label='Anhang')

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data['email'] and not cleaned_data['phone']:
            raise forms.ValidationError('Either email or phone is needed')
        else:
            return cleaned_data
