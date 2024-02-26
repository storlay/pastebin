from django.urls import path
from .views import *

urlpatterns = [
    path('', InputTextView.as_view(), name='input_text'),
    path('message/<int:pk>/', ShowMessageView.as_view(), name='show_message'),
    path('message-feed/', MessageFeedView.as_view(), name='message_feed'),
    path('my-messages/', UserMessageFeedView.as_view(), name='user_message_feed')
]
