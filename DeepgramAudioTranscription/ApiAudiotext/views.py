from typing import Any
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http.response import JsonResponse
from .controllers import TranscriberController

# Create your views here.


class TranscriptionView(View):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.transcriber = TranscriberController('api_key')

    async def post(self, request):
        try:
            audio_file = request.FILES['audio_file']
            minetype = audio_file.content_type
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        response  = await self.transcriber.transcribe(audio_file.read(), minetype)
        return JsonResponse(response, status=200)
    
    def get(self, request):
        return HttpResponse('Hello World')