from django import forms
from django.forms import ModelForm
from .models import Contact
from .models import Quote


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'

