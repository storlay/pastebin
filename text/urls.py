from django.urls import path
from .views import *

urlpatterns = [
    path('', InputTextView.as_view(), name='input_text'),
    path('message/<int:pk>/', ShowMessageView.as_view(), name='show_message')
]
