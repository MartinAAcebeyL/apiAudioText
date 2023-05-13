from django.views import View
from django.http.response import JsonResponse
from .controllers import TranscriberController
import os
from dotenv import load_dotenv

load_dotenv()
# Create your views here.


class TranscriptionView(View):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.transcriber = TranscriberController(os.getenv('DEEPGRAM_API_KEY'))

    async def post(self, request):
        try:
            print(request.FILES)
            audio_file = request.FILES['audio']
            minetype = audio_file.content_type
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        response = await self.transcriber.transcribe(audio_file.read(), minetype)
        return JsonResponse(response, status=200)

    async def get(self, request):
        return JsonResponse({'message': 'Hello World'}, status=200)
