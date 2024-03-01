import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView

from drive.message import download_message
from text.forms import InputTextForm
from text.hash_generation import hash_decode
from text.models import Text
from text.service import create_message


class InputTextView(View):
    def get(self, request):
        return render(request, 'input_text.html', {'form': InputTextForm})

    def post(self, request):
        form = InputTextForm(request.POST)
        if form.is_valid():
            uuid_url = uuid.uuid4()
            author = self.request.user if self.request.user.is_authenticated else None
            create_message(form, uuid_url, author)
            return redirect('show_message', uuid_url)


@method_decorator(cache_page(60), name='dispatch')
class ShowMessageView(DetailView):
    model = Text
    template_name = 'message.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message_object = get_object_or_404(Text, uuid_url=self.kwargs['uuid_url'])
        drive_id = hash_decode(message_object.drive_id)
        context['content'] = download_message(drive_id)
        return context

    def get_object(self, queryset=None):
        return Text.objects.get(uuid_url=self.kwargs['uuid_url'])


@method_decorator(cache_page(15), name='dispatch')
class MessageFeedView(ListView):
    model = Text
    template_name = 'message_feed.html'
    context_object_name = 'messages'
    paginate_by = 9
    queryset = Text.objects.filter(is_private=False)


@method_decorator(cache_page(15), name="dispatch")
class UserMessageFeedView(LoginRequiredMixin, ListView):
    model = Text
    template_name = 'user_message_feed.html'
    context_object_name = 'messages'
    paginate_by = 6

    def get_queryset(self):
        return Text.objects.filter(author_id=self.request.user.pk)
