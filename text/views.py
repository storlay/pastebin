from django.shortcuts import render
from django.views.generic import CreateView

from text.forms import TextForm
from text.models import Text


class InputTextView(CreateView):
    model = Text
    form_class = TextForm

