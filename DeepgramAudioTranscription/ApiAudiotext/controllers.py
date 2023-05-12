from deepgram import Deepgram


class TranscriberController:
    def __init__(self, api_key: str):
        self.deepgram = Deepgram(api_key)

    async def transcribe(self, audio, mimetype):
        source = {'buffer': audio, 'mimetype': mimetype}
        response = await self.deepgram.transcription.prerecorded(
            source, {'language': 'es', 'punctuate': True})
        return response
