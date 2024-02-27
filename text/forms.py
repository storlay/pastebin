from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class InputTextForm(forms.Form):
    message = forms.CharField(label='Сообщение', required=True,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 7}))
    is_temporary = forms.BooleanField(label='Временное сообщение', required=False,
                                      widget=forms.CheckboxInput(attrs={'class': 'form-check-input',
                                                                        'role': 'switch',
                                                                        'id': 'is_temporary',
                                                                        'onchange': "toggleFieldActivation()"}))
    datetime_of_deletion = forms.DateTimeField(label='Дата и время уничтожения сообщения*', required=False,
                                               widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                                 'type': 'datetime-local',
                                                                                 'id': 'datetime_of_deletion',
                                                                                 'disabled': 'disabled'}))

    def clean_datetime_of_deletion(self):
        data = self.cleaned_data['datetime_of_deletion']
        if data is not None and timezone.now() >= data:
            raise ValidationError('Дата и время уничтожения сообщения не могут быть меньше текущих')
        return data
