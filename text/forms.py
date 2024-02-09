from django import forms
from django.forms import ModelForm

from text.models import Text


class InputTextForm(ModelForm):
    url_hash = forms.CharField(label='Введите текст', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Text
        fields = ('url_hash',)