from django.shortcuts import render
from django.views.generic import CreateView

from text.forms import InputTextForm
from text.models import Text


class InputTextView(CreateView):
    model = Text
    form_class = InputTextForm
    template_name = 'index.html'
    success_url = '/'
