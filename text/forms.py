from django import forms
from django.forms import ModelForm

from text.models import Text


class TextForm(ModelForm):
    forms = forms.Textarea()

    class Meta:
        model = Text
        fields = ('text',)
        labels = {
            'text': 'Введите текст'
        }
