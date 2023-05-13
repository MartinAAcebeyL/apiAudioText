from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class TranscriptionViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('transcription')

    def test_post_with_valid_file(self):
        with open('./../files/audio.mp3', 'rb') as f:
            response = self.client.post(self.url, {'audio': f})
            self.assertEqual(response.status_code, 200)

    def test_post_with_invalid_file(self):
        with open('./../files/image.png', 'rb') as f:
            response = self.client.post(self.url, {'audio': f})
            self.assertEqual(response.status_code, 400)

    def test_post_with_empty_request(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 400)