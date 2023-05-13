from django.views import View
from django.http.response import JsonResponse
from .controllers import TranscriberController
import os
from dotenv import load_dotenv
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
load_dotenv()
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class TranscriptionView(View):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.transcriber = TranscriberController(os.getenv('DEEPGRAM_API_KEY'))

    async def post(self, request):
        try:
            audio_file = request.FILES['audio']
            if not audio_file.content_type.startswith('audio/'):
                return JsonResponse({'error': 'Invalid file format. Only audio files.'}, status=400)
            minetype = audio_file.content_type
        except KeyError:
            return JsonResponse({'error': 'Audio file not found.'}, status=400)
        response = await self.transcriber.transcribe(audio_file.read(), minetype)
        transcription = response.get('results').get(
            'channels')[0].get('alternatives')[0].get('transcript')
        return JsonResponse({"transcript": transcription}, status=200)


"""
curl -c cookie.txt -X GET http://localhost:8000/api/transcription/ && 
csrftoken=$(grep -oP '(?<=csrftoken\s)[^;]+' cookie.txt) &&
curl -X POST -H 'X-CSRFToken: $csrftoken' -F 'audio=@/home/martindev/Documentos/github/apiAudioText/audios/cuentan_que_hace_mucho_tiempo.mp3' http://localhost:8000/api/transcription/
 
"""
