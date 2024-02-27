from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from drive.message import download_message
from text.forms import InputTextForm
from text.models import Text


class InputTextView(CreateView):
    model = Text
    form_class = InputTextForm
    template_name = 'input_text.html'
    success_url = reverse_lazy('input_text')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)


class ShowMessageView(DetailView):
    model = Text
    template_name = 'message.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message_object = get_object_or_404(Text, uuid_url=self.kwargs['uuid_url'])
        context['content'] = download_message(message_object.drive_id)
        return context

    def get_object(self, queryset=None):
        return Text.objects.get(uuid_url=self.kwargs['uuid_url'])


class MessageFeedView(ListView):
    model = Text
    template_name = 'message_feed.html'
    context_object_name = 'messages'


class UserMessageFeedView(LoginRequiredMixin, ListView):
    model = Text
    template_name = 'user_message_feed.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Text.objects.filter(author_id=self.request.user.pk)
