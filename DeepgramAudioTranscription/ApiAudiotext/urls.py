from django.urls import path
from .views import TranscriptionView

urlpatterns = [
    path('transcription/', TranscriptionView.as_view(), name='transcription'),
]
