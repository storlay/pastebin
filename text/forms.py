import uuid

from django import forms
from django.core.exceptions import ValidationError

from django.utils import timezone

from pcloud_api.message import upload_message
from text.models import Text


class InputTextForm(forms.ModelForm):
    def clean_datetime_of_deletion(self):
        data = self.cleaned_data['datetime_of_deletion']
        if data is not None and timezone.now() >= data:
            raise ValidationError('Дата и время уничтожения сообщения не могут быть меньше текущих')
        return data

    def save(self, *args, **kwargs):
        result = super(InputTextForm, self).save(commit=False)
        message = self.cleaned_data['url_hash']
        message_hash = uuid.uuid4()
        with open(f'{message_hash}.txt', 'w') as file:
            file.write(message)
        upload_message(f'{message_hash}.txt')
        result.url_hash = message_hash

        result.save(*args, **kwargs)
        return result

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
