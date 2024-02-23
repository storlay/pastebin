from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView

from drive.message import download_message
from text.forms import InputTextForm
from text.models import Text


class InputTextView(CreateView):
    model = Text
    form_class = InputTextForm
    template_name = 'index.html'
    success_url = '/'


class ShowMessageView(DetailView):
    model = Text
    template_name = 'message.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message_object = get_object_or_404(Text, pk=self.kwargs['pk'])
        context['content'] = download_message(message_object.url_hash)
        return context


class MessageFeedView(ListView):
    model = Text
    template_name = 'message_feed.html'
    context_object_name = 'messages'
