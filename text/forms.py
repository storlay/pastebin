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

    def save(self, commit=True):
        result = super(InputTextForm, self).save(commit=False)
        message = self.cleaned_data['drive_id']
        message_name = f'{uuid.uuid4()}.txt'
        with open(message_name, 'w') as file:
            file.write(message)
        message_id = upload_message(message_name)
        result.drive_id = message_id

        result.save()
        return result

    class Meta:
        model = Text
        fields = ('drive_id', 'is_temporary', 'datetime_of_deletion')
        required = ('drive_id',)
        labels = {
            'drive_id': 'Сообщение',
            'is_temporary': 'Временное сообщение',
            'datetime_of_deletion': 'Дата и время уничтожения сообщения*'
        }
        widgets = {
            'drive_id': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
            'is_temporary': forms.CheckboxInput(attrs={'class': 'form-check-input',
                                                       'role': 'switch',
                                                       'id': 'is_temporary',
                                                       'onchange': "toggleFieldActivation()"}),
            'datetime_of_deletion': forms.DateTimeInput(attrs={'class': 'form-control',
                                                               'type': 'datetime-local',
                                                               'id': 'datetime_of_deletion',
                                                               'disabled': 'disabled'})
        }
