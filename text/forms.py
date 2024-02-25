import uuid

from django import forms
from django.core.exceptions import ValidationError

from django.utils import timezone

from drive.message import upload_message
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
        message_name = f'{uuid.uuid4()}.txt'
        with open(message_name, 'w') as file:
            file.write(message)
        message_id = upload_message(message_name)
        result.url_hash = message_id

        result.save(*args, **kwargs)
        return result

    class Meta:
        model = Text
        fields = ('url_hash', 'is_temporary', 'datetime_of_deletion')
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
