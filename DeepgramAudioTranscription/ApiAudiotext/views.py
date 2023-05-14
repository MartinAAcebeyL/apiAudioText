import os
from dotenv import load_dotenv
from django.views import View
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .controllers import TranscriberController

load_dotenv()


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
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        response = await self.transcriber.transcribe(audio_file.read(), minetype)
        transcription = response.get('results').get(
            'channels')[0].get('alternatives')[0].get('transcript')
        return JsonResponse({"transcript": transcription}, status=200)
