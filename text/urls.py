from django.urls import path
from .views import *

urlpatterns = [
    path('', InputTextView.as_view(), name='input_text')
]
