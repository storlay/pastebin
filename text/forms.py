from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

from text.models import Text


class InputTextForm(forms.ModelForm):
    def clean_datetime_of_deletion(self):
        data = self.cleaned_data['datetime_of_deletion']
        if data is not None and datetime.now() >= data:
            raise ValidationError('Дата и время уничтожения сообщения не могут быть меньше текущих')
        return data

    class Meta:
        model = Text
        fields = '__all__'
        required = ('url_hash',)
        labels = {
            'url_hash': 'Сообщение',
            'is_temporary': 'Временное сообщение',
            'datetime_of_deletion': 'Дата и время уничтожения сообщения*'
        }
        widgets = {
            'url_hash': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
            'is_temporary': forms.CheckboxInput(attrs={'class': 'form-check-input',
                                                       'id': 'is_temporary',
                                                       'onchange': "toggleFieldActivation()"}),
            'datetime_of_deletion': forms.DateTimeInput(attrs={'class': 'form-control',
                                                               'type': 'datetime-local',
                                                               'id': 'datetime_of_deletion',
                                                               'disabled': 'disabled'})
        }
